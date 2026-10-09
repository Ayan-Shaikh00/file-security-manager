# File Security Manager

SPPU BSc Cyber Security mini project. Encrypt/decrypt files (AES-256-GCM), SHA-256 integrity check, login, and activity log.

## Run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open https://file-security-manager.onrender.com/login

1. Register → Login
2. Encrypt a file with a password (downloads `.fsm`)
3. Decrypt with the same password
4. Hash a file (optional: paste expected hash to verify)

Keep the file password yourself. It is not saved on the server.

Max file size: 16 MB.
