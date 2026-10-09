# A Mini Project Report

## On

# FILE SECURITY MANAGER

**Submitted in partial fulfilment of the requirements of the degree of**

**Bachelor of Science (Cyber Security)**

**Savitribai Phule Pune University**  
**(2024 Pattern)**

**Submitted by**

| Name | Class | Semester | Roll No. / PRN |
| --- | --- | --- | --- |
| Ayten | S.Y. B.Sc. (Cyber Security) | III | ________________ |

**Under the guidance of**

**Prof. ________________________**

**Department of Cyber Security**  
**[College Name], [City]**  
**Academic Year 2025–26**

---

## Certificate

This is to certify that the mini project report entitled **“File Security Manager”** submitted by **Ayten** in partial fulfilment of the requirements of S.Y. B.Sc. (Cyber Security), Semester–III, Savitribai Phule Pune University (2024 Pattern), is a bona fide record of work carried out under my guidance.

The work embodied in this report has not been submitted elsewhere for any other degree or diploma.

| | |
| --- | --- |
| Project Guide | Head of Department |
| ________________ | ________________ |
| Internal Examiner | External Examiner |
| ________________ | ________________ |
| Place: ____________ | Date: ____________ |

---

## Acknowledgement

I sincerely thank my project guide, the Head of the Department, and the faculty of the Department of Cyber Security for their guidance during this mini project. I also thank Savitribai Phule Pune University for providing the Mini Project course, which allowed me to apply classroom concepts of cryptography, integrity, and access control to a working system.

---

## Title

**File Security Manager: A Web-Based System for Confidentiality, Integrity Verification and Accountable File Operations**

*(Short title for cover page: **File Security Manager**)*

---

## Abstract

Confidentiality and integrity of digital files are essential requirements in academic, personal and organisational environments. Ordinary file storage does not prevent unauthorised reading, does not prove whether a file has been altered, and does not keep a record of security-related actions. This mini project presents **File Security Manager**, a lightweight web application that allows an authenticated user to encrypt a file, decrypt a previously protected file, compute a SHA-256 digest, and view an activity log.

Confidentiality is achieved using **AES-256 in Galois/Counter Mode (GCM)**. The encryption key is not stored on the server; it is derived from a user-supplied file password with **PBKDF2-HMAC-SHA256**. Integrity can be checked independently with **SHA-256**. Application access is controlled through registration and login, with passwords stored as one-way hashes. The system is implemented with **Python (Flask)**, **HTML/CSS/JavaScript**, **Tailwind CSS**, **SQLite** and the **cryptography** library. The scope is deliberately limited to a laboratory-scale mini project and is suitable for demonstration, viva and further academic extension.

**Keywords:** File encryption, AES-256-GCM, SHA-256, PBKDF2, access control, audit log, Flask.

---

## 1. Introduction

Information stored in files is frequently copied, shared through removable media, or kept on personal computers without cryptographic protection. If an unauthorised person obtains such a file, its contents can be read in clear text. If the file is modified, the owner may not notice the change. Traditional operating-system permissions are useful, but they do not protect a file once it has left the original machine, and they do not provide a simple way for a student or small office user to verify integrity.

Cryptography provides well-established answers to these problems. Symmetric encryption protects confidentiality. Cryptographic hash functions support integrity verification. Access control and logging support accountability. The present work combines these ideas in a single, easy-to-use web interface.

The **File Security Manager** is designed as a **Semester-III Mini Project** under the B.Sc. (Cyber Security) 2024 pattern of Savitribai Phule Pune University. The emphasis is on correct use of standard algorithms, a clear architecture, and a working prototype rather than on a commercial product. A user can register, log in, encrypt a selected file with a password, download a protected `.fsm` file, later decrypt it with the same password, generate a SHA-256 hash, optionally compare it with a previously known digest, and inspect recent operations in an activity log.

The remainder of this report describes the proposed system, objectives, methodology, requirements, analysis, tools, test cases, security recommendations, conclusion, future enhancements and references.

---

## 2. Proposed System

The proposed system is a **local web-based File Security Manager**. The browser is used only for the user interface. All cryptographic operations are performed on the **Python Flask** server.

### 2.1 System overview

1. The user registers and logs in.  
2. After authentication, the dashboard presents three operations: **Encrypt**, **Decrypt** and **SHA-256 Hash**.  
3. For encryption, the user uploads a file and enters a **file password** (separate from the login password). The server derives a 256-bit key, encrypts the file with AES-GCM, and returns a `.fsm` file.  
4. For decryption, the user uploads the `.fsm` file and the same password. A wrong password or a damaged file is rejected and recorded in the log.  
5. For hashing, the user uploads any file; the SHA-256 digest is displayed. An optional expected hash can be supplied for comparison.  
6. Each successful or failed security action is written to an **activity log** stored in SQLite.

### 2.2 Encrypted file format

The encrypted file begins with a magic header `FSM1`, followed by the original file name, a random **salt** (16 bytes), a random **nonce** (12 bytes) and the AES-GCM ciphertext (which includes an authentication tag). This format allows the system to restore the original name after decryption and to detect tampering or an incorrect password.

### 2.3 Design principles

- **Confidentiality:** AES-256-GCM.  
- **Integrity of ciphertext:** GCM authentication tag.  
- **Integrity of any file:** SHA-256.  
- **Key secrecy:** file password is not stored; PBKDF2 with 200,000 iterations resists simple brute-force on weak passwords better than a single hash.  
- **Accountability:** per-user logs.  
- **Simplicity:** single application, SQLite database, 16 MB upload limit, suitable for mini-project demonstration.

### 2.4 Architecture

```
User (Browser: HTML, Tailwind CSS, JS)
        |
        | HTTP (login session)
        v
Flask application (Python)
        |
        +-- Access control (session + hashed login password)
        +-- AES-256-GCM encrypt / decrypt (cryptography library)
        +-- SHA-256 hashing (hashlib)
        +-- SQLite (users, logs)
        +-- Temporary upload/download files
```

---

## 3. Objectives

The objectives of this mini project are:

1. To study and apply **symmetric encryption** for protecting file confidentiality.  
2. To implement **AES-256-GCM** with a password-based key derived using **PBKDF2**.  
3. To provide **SHA-256** based integrity verification of files.  
4. To restrict tool usage through **user registration and login**.  
5. To maintain an **audit trail** of encrypt, decrypt and hash operations.  
6. To develop a simple **web interface** using HTML, CSS (Tailwind) and a Python backend.  
7. To demonstrate the working system with defined **test cases** for academic evaluation.

---

## 4. Methodology

The project followed a **simple Software Development Life Cycle** appropriate for a mini project: requirement study, design, implementation, testing and documentation.

### 4.1 Phase I — Requirement study

The problem of unprotected files was identified. Functional needs (encrypt, decrypt, hash, login, log) and non-functional needs (ease of use, local deployment, limited file size) were listed.

### 4.2 Phase II — Design

A three-layer design was chosen:

- **Presentation layer:** login, register and dashboard pages.  
- **Application layer:** Flask routes for authentication and file operations.  
- **Data layer:** SQLite tables `users` and `logs`.

The cryptographic flow was fixed as: salt → PBKDF2 → AES-GCM encrypt/decrypt.

### 4.3 Phase III — Implementation

Python Flask was used for routing and sessions. Werkzeug was used for password hashing of login credentials. The `cryptography` package provided AESGCM and PBKDF2HMAC. Jinja2 templates with Tailwind CSS (CDN) formed the user interface.

### 4.4 Phase IV — Testing

Black-box tests were executed for registration, invalid login, encryption, correct decryption, incorrect password, hash generation and log entries.

### 4.5 Phase V — Documentation

This report records title, abstract, analysis, tools, test cases, security advice, conclusion and bibliography as required for university submission.

---

## 5. Requirement Gathering

### 5.1 Stakeholders

- **Student user:** needs an easy way to protect and verify files.  
- **Examiner / guide:** needs a demonstrable cyber-security mini project with clear algorithms.  
- **Administrator (future):** would need user management; currently each user manages only own logs.

### 5.2 Functional requirements

| ID | Requirement |
| --- | --- |
| FR1 | The system shall allow a new user to register with a unique username. |
| FR2 | The system shall authenticate a registered user before showing file tools. |
| FR3 | The system shall encrypt an uploaded file using AES-256-GCM and a user password. |
| FR4 | The system shall allow download of the encrypted `.fsm` file. |
| FR5 | The system shall decrypt a valid `.fsm` file when the correct password is given. |
| FR6 | The system shall refuse decryption when the password is wrong or the file is not in FSM format. |
| FR7 | The system shall compute SHA-256 of an uploaded file. |
| FR8 | The system shall optionally compare the digest with a user-supplied expected hash. |
| FR9 | The system shall record encrypt, decrypt, decrypt-failure and hash events in a log. |
| FR10 | The system shall allow the user to log out. |

### 5.3 Non-functional requirements

| ID | Requirement |
| --- | --- |
| NFR1 | The interface shall be usable through a common web browser. |
| NFR2 | Cryptographic operations shall use standard libraries, not self-invented ciphers. |
| NFR3 | Login passwords shall not be stored in plain text. |
| NFR4 | File encryption passwords shall not be stored in the database. |
| NFR5 | Maximum upload size shall be limited (16 MB) for laboratory use. |
| NFR6 | The application shall run locally for demonstration (localhost). |

### 5.4 Assumptions and constraints

- The user remembers the file password; there is no password-recovery for encrypted files (by design).  
- The prototype is not deployed on the public Internet.  
- The project does not replace full disk encryption or enterprise Digital Rights Management.

---

## 6. System Analysis

### 6.1 Existing system

Users commonly keep files in folders without encryption. Some use ZIP passwords or third-party tools. ZIP passwords are often weak; many tools do not show integrity hashes or an audit log; cloud services require trust in an external provider.

### 6.2 Limitations of the existing system

- Clear-text files are readable if the device or USB drive is stolen.  
- Changes to a file are not automatically detected.  
- There is no simple local log of who encrypted or hashed a file.  
- Students lack a single teaching tool that combines confidentiality, integrity and access control.

### 6.3 Feasibility

- **Technical:** Python, Flask and AES-GCM are freely available and well documented.  
- **Operational:** A browser and a local server are sufficient for viva demonstration.  
- **Economic:** All tools used are open source; no licence cost.  
- **Schedule:** Scope is limited to core features, which suits a semester mini project.

### 6.4 Data flow (brief)

1. **Register/Login:** username and password → hash stored / verified → session.  
2. **Encrypt:** file bytes + password → salt, nonce, ciphertext → `.fsm` download → log.  
3. **Decrypt:** `.fsm` + password → authenticated decrypt → original file → log.  
4. **Hash:** file bytes → SHA-256 hex digest → display and log.

### 6.5 Use cases

| Use case | Actor | Description |
| --- | --- | --- |
| UC1 Register | User | Create a local account. |
| UC2 Login | User | Authenticate and open dashboard. |
| UC3 Encrypt file | User | Protect a file and download `.fsm`. |
| UC4 Decrypt file | User | Recover original file. |
| UC5 Hash file | User | Obtain or verify SHA-256. |
| UC6 View log | User | See recent security actions. |
| UC7 Logout | User | End the session. |

---

## 7. Tools Used

| Layer | Tool / Technology | Purpose |
| --- | --- | --- |
| Language | Python 3 | Backend logic and cryptography |
| Web framework | Flask | Routes, sessions, file upload/download |
| Cryptography | cryptography (AESGCM, PBKDF2HMAC) | File encryption and key derivation |
| Hashing | hashlib (SHA-256) | File integrity |
| Password hashing | Werkzeug | Safe storage of login passwords |
| Database | SQLite | Users and activity logs |
| Frontend markup | HTML5 | Structure of pages |
| Styling | Tailwind CSS (CDN) | Presentation |
| Scripting | JavaScript (minimal, via Tailwind CDN) | UI support |
| Templates | Jinja2 | Server-side HTML rendering |
| IDE | Cursor / VS Code (or similar) | Development |
| Browser | Chrome / Firefox / Edge | Testing the interface |
| Operating system | Linux (also portable to Windows) | Host environment |
| Version control | Git | Source tracking |

**Hardware (minimum):** PC with 4 GB RAM, any recent CPU, network not required except for Tailwind CDN during UI load (or cache the CSS for fully offline demo).

---

## 8. Test Cases

| TC ID | Test condition | Input | Expected result | Actual result | Status |
| --- | --- | --- | --- | --- | --- |
| TC01 | New user registration | Unique username and password | Account created; redirect to login | Account created message shown | Pass |
| TC02 | Duplicate username | Existing username | Error: username already exists | Error displayed | Pass |
| TC03 | Invalid login | Wrong password | Error: invalid credentials | Error displayed | Pass |
| TC04 | Valid login | Correct username and password | Dashboard with encrypt/decrypt/hash | Dashboard opened | Pass |
| TC05 | Encrypt without file or password | Incomplete form | Operation rejected | Validation / error | Pass |
| TC06 | Encrypt a sample text file | File + password | Download of `.fsm` starting with header `FSM1` | `.fsm` downloaded | Pass |
| TC07 | Decrypt with correct password | `.fsm` + same password | Original file contents restored | Original text recovered | Pass |
| TC08 | Decrypt with wrong password | `.fsm` + wrong password | Error; no plaintext | Failure logged as DECRYPT_FAIL | Pass |
| TC09 | SHA-256 of known file | Sample file | Digest matches independent `sha256sum` | Digests matched | Pass |
| TC10 | Hash verification (match) | File + correct expected hash | Message: hash matches | Match indicated | Pass |
| TC11 | Hash verification (mismatch) | File + incorrect expected hash | Message: possible tampering | Mismatch indicated | Pass |
| TC12 | Activity log | After encrypt/decrypt/hash | Corresponding rows in log table | ENCRYPT, DECRYPT, HASH, DECRYPT_FAIL recorded | Pass |
| TC13 | Unauthenticated access | Open `/dashboard` without login | Redirect to login | Redirected | Pass |
| TC14 | Logout | Click logout | Session cleared; login page | Login shown | Pass |
| TC15 | Oversized file | File larger than 16 MB | Request rejected by server | Size limit applied | Pass |

*(Examiner may ask the student to repeat TC06–TC09 during viva.)*

---

## 9. Security Recommendations

The following recommendations are for **hardening this academic prototype** and for **safe use of file encryption in general**. They do not describe attacks.

1. **Use a strong file password.** Short or dictionary passwords weaken PBKDF2. Prefer a long passphrase known only to the owner.  
2. **Do not reuse the login password as the file password.** Login credentials and encryption secrets should remain separate.  
3. **Never store the file password in a text file next to the `.fsm` file.** Loss of both together defeats encryption.  
4. **Replace the default Flask `secret_key`** before any non-classroom deployment; keep it in an environment variable.  
5. **Do not expose the application to the public Internet** in its present form. It is intended for localhost / lab demonstration.  
6. **Enable HTTPS** if the system is ever placed on a network, so passwords are not sent in clear text.  
7. **Delete temporary files** in the uploads folder after demonstration; they may contain plaintext after decrypt.  
8. **Keep Python and libraries updated** so known defects in dependencies are patched.  
9. **Treat SHA-256 as integrity, not as encryption.** A hash does not hide file contents.  
10. **Back up `.fsm` files**, but remember that a lost password means the data cannot be recovered—this is expected of proper encryption.  
11. **For production systems**, add account lockout, HTTPS, role-based access, hardware-backed keys or OS key stores, and a formal backup policy. Those items are beyond the mini-project scope.

---

## 10. Project Report (Work Summary)

This section summarises what was actually built and submitted.

**Project title:** File Security Manager  
**Course:** B.Sc. (Cyber Security), SPPU 2024 Pattern  
**Class / Semester:** S.Y. / Semester III  
**Type:** Mini Project (working prototype)

**Modules completed**

| Module | Description |
| --- | --- |
| Authentication | Register, login, logout; passwords hashed |
| Encryption module | AES-256-GCM, PBKDF2, `.fsm` download |
| Decryption module | Header parse, authenticated decrypt, original name restore |
| Integrity module | SHA-256 generate and optional verify |
| Logging module | SQLite activity log per user |
| User interface | Responsive dark-themed web pages (Tailwind CSS) |

**How to run (for examiner)**

```text
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` → Register → Login → Encrypt / Decrypt / Hash.

**Learning outcomes**

- Practical use of AES-GCM and password-based key derivation.  
- Difference between encryption (confidentiality) and hashing (integrity).  
- Need for access control and logging in a security tool.  
- Basic full-stack construction of a cyber-security mini project.

---

## 11. Conclusion

The mini project **File Security Manager** successfully demonstrates a compact but complete approach to file protection for academic use. Confidentiality is provided by **AES-256-GCM**, key material is derived with **PBKDF2**, integrity can be verified with **SHA-256**, and users are authenticated before they can operate on files. An activity log supports accountability during demonstration.

The system meets the stated objectives of a Semester-III mini project: it is implementable, explainable in viva, and based on standard cryptographic primitives rather than ad-hoc methods. Limitations such as local deployment, a 16 MB file limit, and the absence of password recovery are accepted as part of the academic scope.

---

## 12. Future Enhancement

The following extensions may be taken up in later semesters or as a major project:

1. **HTTPS deployment** on a college intranet with a proper secret key and hardened server configuration.  
2. **Role-based access control** (student, faculty, administrator).  
3. **Secure file shredding** (overwrite before delete) of temporary plaintext.  
4. **Multiple-file / folder encryption** and progress indication for larger files.  
5. **Key file or hardware token** as an alternative to a typed password.  
6. **Digital signatures** (e.g. Ed25519) for origin authentication in addition to hashing.  
7. **Two-factor authentication** for the web login.  
8. **Administrator dashboard** with filtered logs and export to PDF.  
9. **Mobile-responsive PWA** or a simple desktop installer.  
10. **Formal security testing** (configuration review, dependency audit) under faculty supervision.

---

## 13. Bibliography / References

[1] W. Stallings, *Cryptography and Network Security: Principles and Practice*, Pearson Education.  
[2] B. Schneier, *Applied Cryptography*, John Wiley & Sons.  
[3] NIST, *Advanced Encryption Standard (AES)*, FIPS Publication 197, National Institute of Standards and Technology.  
[4] NIST, *Recommendation for Block Cipher Modes of Operation: Galois/Counter Mode (GCM)*, SP 800-38D.  
[5] NIST, *Secure Hash Standard (SHS)*, FIPS Publication 180-4.  
[6] NIST, *Recommendation for Password-Based Key Derivation*, SP 800-132 (PBKDF2).  
[7] Pallets Projects, *Flask Documentation*, https://flask.palletsprojects.com/  
[8] PyCA, *cryptography (Python library) documentation*, https://cryptography.io/  
[9] SQLite Development Team, *SQLite Documentation*, https://www.sqlite.org/docs.html  
[10] Tailwind Labs, *Tailwind CSS Documentation*, https://tailwindcss.com/docs  
[11] Savitribai Phule Pune University, *B.Sc. (Cyber Security) 2024 Pattern Syllabus*, Faculty of Science and Technology.  
[12] IETF, *PKCS #5: Password-Based Cryptography Specification Version 2.0*, RFC 2898.

---

## Appendix A — List of Abbreviations

| Abbreviation | Expansion |
| --- | --- |
| AES | Advanced Encryption Standard |
| GCM | Galois/Counter Mode |
| PBKDF2 | Password-Based Key Derivation Function 2 |
| SHA | Secure Hash Algorithm |
| SQL | Structured Query Language |
| SPPU | Savitribai Phule Pune University |
| UI | User Interface |
| HTTP | Hypertext Transfer Protocol |

## Appendix B — Project File Structure

```text
file-security-manager/
  app.py
  requirements.txt
  README.md
  templates/
    base.html
    login.html
    register.html
    dashboard.html
  instance/          (created at runtime: fsm.db)
  uploads/           (temporary processed files)
```

---

**Declaration**

I, **Ayten**, hereby declare that the mini project entitled **File Security Manager** is my original work, carried out as part of S.Y. B.Sc. (Cyber Security) Semester-III, SPPU 2024 Pattern. I have not copied this report from any other student or published source except the references cited.

Signature of Student: ________________  
Date: ________________
