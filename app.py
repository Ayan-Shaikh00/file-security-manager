import hashlib
import os
import sqlite3
import struct
from datetime import datetime
from functools import wraps
from pathlib import Path

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from flask import (
    Flask,
    flash,
    g,
    redirect,
    render_template,
    request,
    send_file,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.environ.get("FSM_SECRET_KEY", "mini-project-change-me")
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "instance" / "fsm.db"
UPLOAD_DIR = BASE_DIR / "uploads"

MAGIC = b"FSM1"
SALT_LEN = 16
NONCE_LEN = 12
KDF_ITERATIONS = 200_000


def get_db():
    if "db" not in g:
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(_exc):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    db.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            action TEXT NOT NULL,
            filename TEXT,
            detail TEXT,
            created_at TEXT NOT NULL
        );
        """
    )
    db.commit()


@app.before_request
def ensure_db():
    init_db()
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("username"):
            return redirect(url_for("login"))
        return view(*args, **kwargs)

    return wrapped


def add_log(action, filename="", detail=""):
    db = get_db()
    db.execute(
        "INSERT INTO logs (username, action, filename, detail, created_at) VALUES (?, ?, ?, ?, ?)",
        (
            session["username"],
            action,
            filename,
            detail,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        ),
    )
    db.commit()


def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=KDF_ITERATIONS,
    )
    return kdf.derive(password.encode("utf-8"))


def encrypt_bytes(data: bytes, password: str, original_name: str) -> bytes:
    salt = os.urandom(SALT_LEN)
    nonce = os.urandom(NONCE_LEN)
    key = derive_key(password, salt)
    ciphertext = AESGCM(key).encrypt(nonce, data, None)
    name_bytes = original_name.encode("utf-8")[:255]
    header = MAGIC + struct.pack("B", len(name_bytes)) + name_bytes + salt + nonce
    return header + ciphertext


def decrypt_bytes(blob: bytes, password: str) -> tuple[bytes, str]:
    if len(blob) < 4 + 1 + SALT_LEN + NONCE_LEN or blob[:4] != MAGIC:
        raise ValueError("Not a File Security Manager encrypted file.")
    name_len = blob[4]
    offset = 5
    name = blob[offset : offset + name_len].decode("utf-8", errors="replace")
    offset += name_len
    salt = blob[offset : offset + SALT_LEN]
    offset += SALT_LEN
    nonce = blob[offset : offset + NONCE_LEN]
    offset += NONCE_LEN
    ciphertext = blob[offset:]
    key = derive_key(password, salt)
    try:
        plain = AESGCM(key).decrypt(nonce, ciphertext, None)
    except Exception as exc:
        raise ValueError("Wrong password or file is damaged.") from exc
    return plain, name or "decrypted_file"


@app.route("/")
def home():
    if session.get("username"):
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = (request.form.get("username") or "").strip()
        password = request.form.get("password") or ""
        if not username or not password:
            flash("Username and password are required.", "error")
            return render_template("register.html")
        db = get_db()
        try:
            db.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, generate_password_hash(password)),
            )
            db.commit()
        except sqlite3.IntegrityError:
            flash("Username already exists.", "error")
            return render_template("register.html")
        flash("Account created. Please login.", "ok")
        return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = (request.form.get("username") or "").strip()
        password = request.form.get("password") or ""
        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        if user is None or not check_password_hash(user["password_hash"], password):
            flash("Invalid username or password.", "error")
            return render_template("login.html")
        session.clear()
        session["username"] = user["username"]
        return redirect(url_for("dashboard"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/dashboard")
@login_required
def dashboard():
    logs = (
        get_db()
        .execute(
            "SELECT * FROM logs WHERE username = ? ORDER BY id DESC LIMIT 20",
            (session["username"],),
        )
        .fetchall()
    )
    return render_template("dashboard.html", logs=logs, hash_result=None)


@app.route("/encrypt", methods=["POST"])
@login_required
def encrypt():
    file = request.files.get("file")
    password = request.form.get("password") or ""
    if not file or not file.filename or not password:
        flash("Choose a file and enter an encryption password.", "error")
        return redirect(url_for("dashboard"))
    original = secure_filename(file.filename) or "file"
    data = file.read()
    blob = encrypt_bytes(data, password, original)
    add_log("ENCRYPT", original, f"{len(data)} bytes")
    out_name = original + ".fsm"
    out_path = UPLOAD_DIR / f"{session['username']}_{out_name}"
    out_path.write_bytes(blob)
    return send_file(out_path, as_attachment=True, download_name=out_name)


@app.route("/decrypt", methods=["POST"])
@login_required
def decrypt():
    file = request.files.get("file")
    password = request.form.get("password") or ""
    if not file or not file.filename or not password:
        flash("Choose an encrypted file and enter the password.", "error")
        return redirect(url_for("dashboard"))
    blob = file.read()
    try:
        plain, original = decrypt_bytes(blob, password)
    except ValueError as exc:
        add_log("DECRYPT_FAIL", file.filename, str(exc))
        flash(str(exc), "error")
        return redirect(url_for("dashboard"))
    add_log("DECRYPT", original, "ok")
    out_path = UPLOAD_DIR / f"{session['username']}_out_{secure_filename(original)}"
    out_path.write_bytes(plain)
    return send_file(out_path, as_attachment=True, download_name=original)


@app.route("/hash", methods=["POST"])
@login_required
def file_hash():
    file = request.files.get("file")
    expected = (request.form.get("expected") or "").strip().lower()
    if not file or not file.filename:
        flash("Choose a file to hash.", "error")
        return redirect(url_for("dashboard"))
    digest = hashlib.sha256(file.read()).hexdigest()
    match = None
    if expected:
        match = digest == expected
    add_log("HASH", secure_filename(file.filename), digest)
    logs = (
        get_db()
        .execute(
            "SELECT * FROM logs WHERE username = ? ORDER BY id DESC LIMIT 20",
            (session["username"],),
        )
        .fetchall()
    )
    return render_template(
        "dashboard.html",
        logs=logs,
        hash_result=digest,
        hash_file=file.filename,
        hash_match=match,
    )


if __name__ == "__main__":
    app.run(debug=True)
