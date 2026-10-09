#!/usr/bin/env python3
"""Write a print-ready HTML report and convert it to PDF with Chrome."""
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent
HTML_PATH = OUT_DIR / "File_Security_Manager_Mini_Project_Report.html"
PDF_PATH = OUT_DIR.parent / "File_Security_Manager_Mini_Project_Report.pdf"

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>File Security Manager — Mini Project Report</title>
<style>
  @page { size: A4; margin: 22mm 20mm 22mm 20mm; }
  * { box-sizing: border-box; }
  body {
    font-family: "Times New Roman", Times, serif;
    font-size: 12pt;
    line-height: 1.55;
    color: #111;
    margin: 0;
  }
  h1 { font-size: 18pt; text-align: center; text-transform: uppercase; margin: 18pt 0 10pt; }
  h2 { font-size: 14pt; margin: 18pt 0 8pt; page-break-after: avoid; }
  h3 { font-size: 13pt; margin: 14pt 0 6pt; page-break-after: avoid; }
  h4 { font-size: 12pt; margin: 12pt 0 6pt; }
  p { text-align: justify; margin: 0 0 8pt; }
  .cover { text-align: center; page-break-after: always; padding-top: 18pt; }
  .cover h1 { font-size: 22pt; letter-spacing: 1px; margin: 16pt 0; }
  .muted { font-size: 11pt; }
  .sign-row { display: flex; justify-content: space-between; margin-top: 36pt; }
  .sign { width: 45%; text-align: center; }
  table { width: 100%; border-collapse: collapse; margin: 8pt 0 12pt; font-size: 11pt; }
  th, td { border: 1px solid #333; padding: 5pt 6pt; vertical-align: top; }
  th { background: #eee; }
  ul, ol { margin: 0 0 10pt 18pt; }
  li { margin-bottom: 3pt; }
  .toc a { color: #000; text-decoration: none; }
  .toc td { border: none; padding: 3pt 0; }
  .toc table { border: none; }
  pre, .code {
    font-family: "Courier New", monospace;
    font-size: 9.5pt;
    background: #f6f6f6;
    border: 1px solid #ccc;
    padding: 8pt;
    white-space: pre-wrap;
    page-break-inside: avoid;
  }
  .center { text-align: center; }
  .page-break { page-break-before: always; }
  .blank { border-bottom: 1px dotted #333; display: inline-block; min-width: 180pt; }
  .kw { font-style: italic; }
  .fig { text-align: center; font-style: italic; font-size: 11pt; margin: 4pt 0 12pt; }
</style>
</head>
<body>

<div class="cover">
  <p class="muted">SAVITRIBAI PHULE PUNE UNIVERSITY</p>
  <p class="muted">(Formerly University of Pune)</p>
  <p><strong>FACULTY OF SCIENCE AND TECHNOLOGY</strong></p>
  <p>B.Sc. (Cyber Security) — 2024 Pattern</p>
  <p style="margin-top:28pt;">A MINI PROJECT REPORT<br/>ON</p>
  <h1>FILE SECURITY MANAGER</h1>
  <p><em>A Web-Based System for Confidentiality, Integrity Verification<br/>and Accountable File Operations</em></p>
  <p style="margin-top:22pt;">Submitted in partial fulfilment of the requirements of the degree of</p>
  <p><strong>BACHELOR OF SCIENCE (CYBER SECURITY)</strong></p>
  <p>Semester — III &nbsp;|&nbsp; Class — S.Y. B.Sc. (Cyber Security)</p>
  <p>Academic Year 2025–26</p>
  <p style="margin-top:28pt;"><strong>Submitted by</strong></p>
  <p>Ayten<br/>Roll No. / PRN: <span class="blank">&nbsp;</span></p>
  <p style="margin-top:18pt;"><strong>Under the guidance of</strong></p>
  <p>Prof. <span class="blank">&nbsp;</span></p>
  <p style="margin-top:28pt;"><strong>Department of Cyber Security</strong><br/>
  [College Name], [City / Pune]</p>
</div>

<h2>CERTIFICATE</h2>
<p>This is to certify that the mini project report entitled <strong>“File Security Manager”</strong> submitted by <strong>Ayten</strong>, student of S.Y. B.Sc. (Cyber Security), Semester–III, is a bona fide record of the work carried out under my supervision and guidance in partial fulfilment of the requirements of Savitribai Phule Pune University (2024 Pattern).</p>
<p>The matter embodied in this report has not been submitted to any other University or Institute for the award of any degree, diploma or certificate.</p>
<div class="sign-row">
  <div class="sign">________________________<br/>Project Guide</div>
  <div class="sign">________________________<br/>Head of Department</div>
</div>
<div class="sign-row">
  <div class="sign">________________________<br/>Internal Examiner</div>
  <div class="sign">________________________<br/>External Examiner</div>
</div>
<p style="margin-top:28pt;">Place: ____________________ &nbsp;&nbsp;&nbsp; Date: ____________________</p>
<p>College Seal:</p>

<div class="page-break"></div>
<h2>DECLARATION</h2>
<p>I, <strong>Ayten</strong>, hereby declare that the mini project entitled <strong>“File Security Manager”</strong> submitted to Savitribai Phule Pune University in partial fulfilment of S.Y. B.Sc. (Cyber Security) Semester–III (2024 Pattern) is my original work. I have not copied this report from any other student, website or published source except the material duly acknowledged in the bibliography. I understand that any academic misconduct may invite disciplinary action as per University rules.</p>
<p style="margin-top:36pt;">Signature of the Student: ________________________</p>
<p>Name: Ayten</p>
<p>Date: ________________________</p>

<h2>ACKNOWLEDGEMENT</h2>
<p>It is a matter of privilege to present this mini project report on <strong>File Security Manager</strong>. I express my sincere gratitude to my project guide, Prof. ____________________, for consistent guidance, timely suggestions and encouragement throughout the work.</p>
<p>I thank the Head of the Department of Cyber Security and all faculty members for providing laboratory facilities and academic support. I am grateful to Savitribai Phule Pune University for including Mini Project in the B.Sc. (Cyber Security) 2024 curriculum, which enabled me to apply classroom concepts of cryptography, hashing, access control and secure software practice to a working system.</p>
<p>I also thank my classmates and family for their cooperation during testing and documentation. Any remaining shortcomings in this report are my own.</p>
<p class="center" style="margin-top:24pt;">— Ayten</p>

<div class="page-break"></div>
<h2>ABSTRACT</h2>
<p>Digital files used in academic and personal work are often stored and shared without cryptographic protection. If a storage device is lost or a file is copied, the contents can be read in clear text. If a file is modified, the owner may not detect the change. Operating-system permissions do not protect a file after it leaves the original computer, and they do not provide a simple integrity check or an audit trail of security operations.</p>
<p>This mini project presents <strong>File Security Manager</strong>, a laboratory-scale web application that allows an authenticated user to (i) encrypt a file, (ii) decrypt a previously protected file, (iii) compute and optionally verify a SHA-256 digest, and (iv) view a personal activity log. Confidentiality is provided by the Advanced Encryption Standard with a 256-bit key in Galois/Counter Mode (AES-256-GCM). The encryption key is not stored on the server; it is derived from a user-supplied file password using PBKDF2-HMAC-SHA256 with a random salt and 200,000 iterations. Ciphertext authenticity is provided by the GCM tag. Independent integrity verification of any file is provided by SHA-256. Application access is controlled by registration and login; login passwords are stored as one-way hashes.</p>
<p>The system is implemented using Python (Flask) on the server and HTML, CSS and Tailwind CSS in the browser. User accounts and logs are stored in SQLite. Encrypted files use a simple portable format with magic header <strong>FSM1</strong>. The scope is deliberately limited to a mini project: local demonstration, a 16 MB upload limit, and no claim of being an enterprise product. The prototype is suitable for practical demonstration, viva-voce and further academic extension.</p>
<p class="kw"><strong>Keywords:</strong> File encryption, AES-256-GCM, SHA-256, PBKDF2, access control, audit log, Flask, mini project, cyber security.</p>

<h2>LIST OF ABBREVIATIONS</h2>
<table>
<tr><th>Abbreviation</th><th>Expansion</th></tr>
<tr><td>AES</td><td>Advanced Encryption Standard</td></tr>
<tr><td>CIA</td><td>Confidentiality, Integrity, Availability</td></tr>
<tr><td>FIPS</td><td>Federal Information Processing Standard</td></tr>
<tr><td>FSM</td><td>File Security Manager (also encrypted file extension .fsm)</td></tr>
<tr><td>GCM</td><td>Galois/Counter Mode</td></tr>
<tr><td>GUI</td><td>Graphical User Interface</td></tr>
<tr><td>HMAC</td><td>Hash-based Message Authentication Code</td></tr>
<tr><td>HTML</td><td>HyperText Markup Language</td></tr>
<tr><td>HTTP</td><td>HyperText Transfer Protocol</td></tr>
<tr><td>NIST</td><td>National Institute of Standards and Technology</td></tr>
<tr><td>PBKDF2</td><td>Password-Based Key Derivation Function 2</td></tr>
<tr><td>SHA</td><td>Secure Hash Algorithm</td></tr>
<tr><td>SPPU</td><td>Savitribai Phule Pune University</td></tr>
<tr><td>SQL</td><td>Structured Query Language</td></tr>
<tr><td>UI</td><td>User Interface</td></tr>
</table>

<div class="page-break"></div>
<h2>TABLE OF CONTENTS</h2>
<div class="toc">
<table>
<tr><td>Certificate</td><td style="text-align:right;">i</td></tr>
<tr><td>Declaration</td><td style="text-align:right;">ii</td></tr>
<tr><td>Acknowledgement</td><td style="text-align:right;">iii</td></tr>
<tr><td>Abstract</td><td style="text-align:right;">iv</td></tr>
<tr><td>List of Abbreviations</td><td style="text-align:right;">v</td></tr>
<tr><td>1. Introduction</td><td style="text-align:right;">1</td></tr>
<tr><td>&nbsp;&nbsp;1.1 Background</td><td style="text-align:right;">1</td></tr>
<tr><td>&nbsp;&nbsp;1.2 Problem Statement</td><td style="text-align:right;">1</td></tr>
<tr><td>&nbsp;&nbsp;1.3 Need of the System</td><td style="text-align:right;">1</td></tr>
<tr><td>&nbsp;&nbsp;1.4 Scope of the Project</td><td style="text-align:right;">2</td></tr>
<tr><td>&nbsp;&nbsp;1.5 Organization of the Report</td><td style="text-align:right;">2</td></tr>
<tr><td>2. Proposed System</td><td style="text-align:right;">3</td></tr>
<tr><td>3. Objectives</td><td style="text-align:right;">5</td></tr>
<tr><td>4. Methodology</td><td style="text-align:right;">6</td></tr>
<tr><td>5. Requirement Gathering</td><td style="text-align:right;">7</td></tr>
<tr><td>6. System Analysis</td><td style="text-align:right;">9</td></tr>
<tr><td>7. Tools Used</td><td style="text-align:right;">12</td></tr>
<tr><td>8. System Design and Implementation</td><td style="text-align:right;">13</td></tr>
<tr><td>9. Test Cases</td><td style="text-align:right;">16</td></tr>
<tr><td>10. Security Recommendations</td><td style="text-align:right;">18</td></tr>
<tr><td>11. Project Work Summary / Report</td><td style="text-align:right;">19</td></tr>
<tr><td>12. Conclusion</td><td style="text-align:right;">20</td></tr>
<tr><td>13. Future Enhancement</td><td style="text-align:right;">21</td></tr>
<tr><td>14. Bibliography</td><td style="text-align:right;">22</td></tr>
<tr><td>Appendix A — File Structure</td><td style="text-align:right;">23</td></tr>
<tr><td>Appendix B — How to Run</td><td style="text-align:right;">23</td></tr>
</table>
</div>

<div class="page-break"></div>
<h2>CHAPTER 1 &nbsp; INTRODUCTION</h2>

<h3>1.1 Background</h3>
<p>Information security is commonly explained through the CIA triad: <strong>Confidentiality</strong> (prevention of unauthorised disclosure), <strong>Integrity</strong> (detection of unauthorised modification) and <strong>Availability</strong> (timely access for authorised users). Files on student laptops, laboratory systems and USB drives frequently fail the first two properties. A Word document, PDF, source-code file or spreadsheet copied from a shared computer can be opened by anyone who obtains it. A tampered assignment or log file may go unnoticed if no cryptographic digest was recorded.</p>
<p>Classical access-control lists of an operating system are necessary but not sufficient. They depend on the same machine and the same user accounts. Cryptography, in contrast, binds protection to the file itself. Symmetric encryption renders the contents unintelligible without a secret. A cryptographic hash produces a fixed-length fingerprint; any change in the file, however small, produces a different digest with overwhelming probability.</p>
<p>The B.Sc. (Cyber Security) programme of Savitribai Phule Pune University (2024 Pattern) includes a Mini Project in Semester III so that students can implement such principles rather than only describe them. <strong>File Security Manager</strong> was selected as a topic because it maps directly onto confidentiality, integrity, authentication and auditing, while remaining small enough to complete within one semester.</p>

<h3>1.2 Problem Statement</h3>
<p>To design and implement a simple web-based File Security Manager that enables a registered user to encrypt and decrypt files using a standard symmetric algorithm, to verify file integrity using SHA-256, and to record security-related actions in an activity log, for laboratory demonstration under SPPU B.Sc. (Cyber Security) Semester–III.</p>

<h3>1.3 Need of the System</h3>
<ul>
<li>Students and small offices share files over USB and cloud folders without encryption.</li>
<li>Password-protected ZIP files are widely used but are often weakly configured and do not teach modern authenticated encryption.</li>
<li>Hash tools exist as command-line utilities; beginners need a unified interface.</li>
<li>There is academic value in showing that encryption (hiding content) and hashing (fingerprinting content) are different services.</li>
<li>An audit log trains the student to think of accountability, not only of algorithms.</li>
</ul>

<h3>1.4 Scope of the Project</h3>
<p><strong>In scope:</strong> user registration and login; AES-256-GCM file encryption and decryption with a password-derived key; SHA-256 generation and optional comparison; SQLite activity log; web UI; local execution; maximum file size 16 MB.</p>
<p><strong>Out of scope:</strong> public Internet deployment, payment/cloud storage, recovery of a forgotten file password, full-disk encryption, steganography, malware analysis, and enterprise key-management systems.</p>

<h3>1.5 Organization of the Report</h3>
<p>Chapter 2 describes the proposed system. Chapter 3 lists objectives. Chapter 4 explains methodology. Chapter 5 records requirement gathering. Chapter 6 presents system analysis. Chapter 7 lists tools. Chapter 8 details design and implementation. Chapter 9 gives test cases. Chapter 10 states security recommendations. Chapter 11 summarises the work. Chapters 12–14 present conclusion, future work and bibliography.</p>

<div class="page-break"></div>
<h2>CHAPTER 2 &nbsp; PROPOSED SYSTEM</h2>

<h3>2.1 Overview</h3>
<p>The proposed system is a <strong>local web application</strong>. The user opens a browser and connects to a Flask server running on the same computer (http://127.0.0.1:5000). The browser displays forms. All cryptographic work is performed in Python so that algorithms can be explained from server-side code during viva.</p>
<p>After login, the dashboard offers three panels: Encrypt, Decrypt and SHA-256 Hash, together with an Activity Log table.</p>

<h3>2.2 Users and roles</h3>
<p>The prototype supports a single role: <strong>registered user</strong>. Each user sees only their own log entries. There is no separate administrator console in this version, which keeps the mini project small.</p>

<h3>2.3 Encryption workflow</h3>
<ol>
<li>The user selects a file and enters a <em>file password</em> (distinct from the login password).</li>
<li>The server reads the file bytes (up to 16 MB).</li>
<li>A 16-byte random salt and a 12-byte random nonce are generated.</li>
<li>PBKDF2-HMAC-SHA256 derives a 32-byte (256-bit) key from the password and salt, using 200,000 iterations.</li>
<li>AES-GCM encrypts the plaintext, producing ciphertext plus an authentication tag.</li>
<li>A header is prepended: magic <code>FSM1</code>, original file-name length and name, salt, nonce, then ciphertext.</li>
<li>The user downloads a file with extension <strong>.fsm</strong>. The event is logged as ENCRYPT.</li>
</ol>

<h3>2.4 Decryption workflow</h3>
<ol>
<li>The user uploads a .fsm file and the same file password.</li>
<li>The server checks the magic header. An invalid file is rejected.</li>
<li>Salt and nonce are read from the header; the key is re-derived with PBKDF2.</li>
<li>AES-GCM decrypts and verifies the tag. A wrong password or a modified file fails authentication.</li>
<li>On success, the original file is returned and DECRYPT is logged. On failure, DECRYPT_FAIL is logged and no plaintext is given.</li>
</ol>

<h3>2.5 Integrity workflow</h3>
<p>The user uploads any file. The server computes SHA-256 and displays the 64-character hexadecimal digest. If the user pastes an expected hash, the system reports match or mismatch. This demonstrates integrity checking without decrypting anything.</p>

<h3>2.6 Design principles</h3>
<ul>
<li><strong>Use standard algorithms only</strong> — AES, GCM, SHA-256, PBKDF2 (NIST / IETF).</li>
<li><strong>Do not store the file password</strong> — recovery is impossible by design if the password is lost.</li>
<li><strong>Authenticated encryption</strong> — GCM detects tampering of ciphertext.</li>
<li><strong>Least surprise UI</strong> — three clear actions on one dashboard.</li>
<li><strong>Accountability</strong> — operations are logged with timestamp, action, file name and detail.</li>
</ul>

<h3>2.7 Logical architecture</h3>
<pre>
  +------------------+          HTTP + session          +-----------------------+
  | Browser          | <------------------------------> | Flask application     |
  | HTML + Tailwind  |                                  | app.py                |
  +------------------+                                  |  - login/register     |
                                                        |  - encrypt/decrypt    |
                                                        |  - hash               |
                                                        |  - logs               |
                                                        +-----------+-----------+
                                                                    |
                                              +---------------------+---------------------+
                                              |                     |                     |
                                        SQLite DB              cryptography            hashlib
                                        users, logs            AES-GCM, PBKDF2         SHA-256
</pre>
<p class="fig">Figure 2.1 &nbsp; High-level architecture of File Security Manager</p>

<h3>2.8 Encrypted file layout</h3>
<pre>
  Offset   Field
  0..3     Magic "FSM1"
  4        Length N of original file name (1 byte)
  5..      File name (N bytes, UTF-8)
  then     Salt (16 bytes)
  then     Nonce (12 bytes)
  then     AES-GCM ciphertext || tag
</pre>
<p class="fig">Figure 2.2 &nbsp; Binary layout of a .fsm file</p>

<div class="page-break"></div>
<h2>CHAPTER 3 &nbsp; OBJECTIVES</h2>
<p>The objectives of this mini project are stated in measurable academic terms:</p>
<ol>
<li>To study the role of cryptography in protecting files at rest, with reference to the CIA triad.</li>
<li>To implement file confidentiality using <strong>AES-256-GCM</strong>, a NIST-recommended authenticated encryption mode.</li>
<li>To derive the encryption key from a user password using <strong>PBKDF2-HMAC-SHA256</strong> with random salt, so that the raw password is not used directly as a key.</li>
<li>To implement file integrity verification using the <strong>SHA-256</strong> hash function, including optional comparison with a previously known digest.</li>
<li>To provide <strong>authentication and access control</strong> so that only a logged-in user can invoke encrypt, decrypt and hash operations.</li>
<li>To store login passwords as <strong>one-way hashes</strong> and never store the file-encryption password in the database.</li>
<li>To maintain a <strong>per-user activity log</strong> for demonstration of auditing.</li>
<li>To develop a usable <strong>web interface</strong> with HTML and Tailwind CSS and a Python Flask backend.</li>
<li>To verify the prototype using a defined set of <strong>test cases</strong> suitable for internal assessment and viva.</li>
<li>To document the work in the format expected for an SPPU mini project report.</li>
</ol>

<h2>CHAPTER 4 &nbsp; METHODOLOGY</h2>
<p>A simplified Software Development Life Cycle (SDLC) was followed. This is appropriate for a one-semester mini project.</p>

<h3>4.1 Requirement study</h3>
<p>Informal interviews with classmates and observation of laboratory file-sharing practice showed that students store assignments in plain folders. Functional needs (encrypt, decrypt, hash, login, log) and constraints (time, no budget, must run on a student PC) were listed. Unrealistic features such as cloud sync were excluded.</p>

<h3>4.2 Design</h3>
<p>A three-tier design was chosen: presentation (templates), application (Flask routes and crypto helpers), and data (SQLite). The cryptographic pipeline was fixed before coding: salt → PBKDF2 → AES-GCM. The .fsm header was specified so that the original file name can be restored.</p>

<h3>4.3 Implementation</h3>
<p>Coding was done in Python 3. Flask handles HTTP, sessions and uploads. Werkzeug hashes login passwords. The PyCA <em>cryptography</em> library supplies AESGCM and PBKDF2HMAC. Jinja2 templates render login, register and dashboard pages styled with Tailwind CSS via CDN.</p>

<h3>4.4 Testing</h3>
<p>Black-box tests were executed through the web forms and through HTTP requests: registration, bad login, encrypt, decrypt with correct and incorrect passwords, hash comparison with an independent SHA-256 tool, and inspection of log rows. Defects (for example missing validation) were corrected before documentation.</p>

<h3>4.5 Documentation</h3>
<p>This report, a README for execution, and comments in source code form the documentation set. The student is expected to explain AES-GCM and SHA-256 in viva without reading the code line by line.</p>

<div class="page-break"></div>
<h2>CHAPTER 5 &nbsp; REQUIREMENT GATHERING</h2>

<h3>5.1 Stakeholders</h3>
<table>
<tr><th>Stakeholder</th><th>Interest</th></tr>
<tr><td>Student / end user</td><td>Easy protection and verification of personal files</td></tr>
<tr><td>Project guide / examiner</td><td>Correct algorithms, working demo, clear report</td></tr>
<tr><td>College laboratory</td><td>Runs on existing PCs without paid software</td></tr>
</table>

<h3>5.2 Functional requirements</h3>
<table>
<tr><th>ID</th><th>Requirement</th><th>Priority</th></tr>
<tr><td>FR1</td><td>The system shall allow a new user to register with a unique username and a password.</td><td>High</td></tr>
<tr><td>FR2</td><td>The system shall authenticate a registered user and create a session.</td><td>High</td></tr>
<tr><td>FR3</td><td>The system shall reject invalid login attempts with a generic error message.</td><td>High</td></tr>
<tr><td>FR4</td><td>The system shall encrypt an uploaded file with AES-256-GCM and a user-supplied file password.</td><td>High</td></tr>
<tr><td>FR5</td><td>The system shall return the ciphertext as a downloadable .fsm file containing a recoverable original name.</td><td>High</td></tr>
<tr><td>FR6</td><td>The system shall decrypt a valid .fsm file when the correct password is supplied.</td><td>High</td></tr>
<tr><td>FR7</td><td>The system shall refuse decryption of a wrong password, damaged file, or non-FSM file, without revealing plaintext.</td><td>High</td></tr>
<tr><td>FR8</td><td>The system shall compute the SHA-256 digest of an uploaded file and display it.</td><td>High</td></tr>
<tr><td>FR9</td><td>The system shall optionally compare the digest with a user-supplied expected hash and report match or mismatch.</td><td>Medium</td></tr>
<tr><td>FR10</td><td>The system shall record encrypt, decrypt, decrypt-failure and hash events with timestamp and username.</td><td>High</td></tr>
<tr><td>FR11</td><td>The system shall allow logout and shall hide tools from unauthenticated visitors.</td><td>High</td></tr>
<tr><td>FR12</td><td>The system shall show flash messages for success and error conditions.</td><td>Medium</td></tr>
</table>

<h3>5.3 Non-functional requirements</h3>
<table>
<tr><th>ID</th><th>Requirement</th><th>Category</th></tr>
<tr><td>NFR1</td><td>Usable in a common desktop browser without a native installer.</td><td>Usability</td></tr>
<tr><td>NFR2</td><td>Cryptography shall use a maintained library, not a student-written cipher.</td><td>Security</td></tr>
<tr><td>NFR3</td><td>Login passwords shall be stored as salted one-way hashes (Werkzeug).</td><td>Security</td></tr>
<tr><td>NFR4</td><td>File passwords shall never be written to SQLite.</td><td>Security</td></tr>
<tr><td>NFR5</td><td>Maximum upload size 16 MB to protect laboratory memory.</td><td>Performance</td></tr>
<tr><td>NFR6</td><td>Application shall start with a short command sequence documented in README.</td><td>Operability</td></tr>
<tr><td>NFR7</td><td>Source code shall remain small enough for viva explanation.</td><td>Maintainability</td></tr>
<tr><td>NFR8</td><td>Intended deployment is localhost / isolated lab, not the public Internet.</td><td>Deployment</td></tr>
</table>

<h3>5.4 Assumptions</h3>
<ul>
<li>The user remembers the file password; there is no “forgot encryption password” feature.</li>
<li>The demonstrator’s PC has Python 3 and a browser.</li>
<li>Files are ordinary documents or binaries within the size limit.</li>
</ul>

<h3>5.5 Constraints</h3>
<ul>
<li>Time: one academic semester mini project.</li>
<li>Budget: free and open-source tools only.</li>
<li>Skill level: second-year undergraduate.</li>
<li>Legal/ethical: the tool is for protecting the owner’s own files, not for hiding evidence or attacking others.</li>
</ul>

<div class="page-break"></div>
<h2>CHAPTER 6 &nbsp; SYSTEM ANALYSIS</h2>

<h3>6.1 Existing system</h3>
<p>In the present academic environment, files are stored in local folders, email attachments and cloud drives. Some users apply ZIP compression with a password. Advanced users may call OpenSSL on the command line. Hash values, when used at all, are computed with separate utilities and copied by hand.</p>

<h3>6.2 Limitations of the existing system</h3>
<ul>
<li>Plain files disclose content after theft of a device or an unlocked session.</li>
<li>ZIP passwords are often short and are not a teaching example of AES-GCM.</li>
<li>Command-line cryptography is powerful but unfriendly for a first demonstration.</li>
<li>Integrity and confidentiality are rarely offered in one student-facing screen.</li>
<li>There is typically no log of who encrypted or hashed a file on a shared laboratory PC.</li>
</ul>

<h3>6.3 Proposed improvements</h3>
<p>File Security Manager unifies login, authenticated encryption, hashing and logging. It uses AES-GCM rather than an obsolete mode. It separates the <em>account password</em> from the <em>file password</em>. It produces a portable .fsm object that can be copied to another machine running the same application.</p>

<h3>6.4 Feasibility study</h3>
<p><strong>Technical feasibility:</strong> Python 3, Flask, SQLite and the cryptography package are available on Linux and Windows. AES-GCM is supported in hardware on modern CPUs but the library also provides a portable implementation.</p>
<p><strong>Operational feasibility:</strong> A viva demonstration needs only a browser and a sample text file. Faculty can encrypt, corrupt a copy, and show that decryption fails.</p>
<p><strong>Economic feasibility:</strong> All components are open source. No licence fee.</p>
<p><strong>Schedule feasibility:</strong> Core modules are few; the scope was frozen early to avoid product-scale features.</p>

<h3>6.5 Data flow (levelled description)</h3>
<p><strong>Login DFD:</strong> User → credentials → verify hash in users table → session cookie → dashboard.</p>
<p><strong>Encrypt DFD:</strong> File + password → key derivation → AES-GCM → .fsm to user; metadata to logs.</p>
<p><strong>Decrypt DFD:</strong> .fsm + password → parse header → AES-GCM open → file to user or error to logs.</p>
<p><strong>Hash DFD:</strong> File → SHA-256 → display; optional compare → logs.</p>

<h3>6.6 Use case summary</h3>
<table>
<tr><th>ID</th><th>Use case</th><th>Actor</th><th>Main success scenario</th></tr>
<tr><td>UC1</td><td>Register</td><td>Visitor</td><td>Unique username stored; redirect to login</td></tr>
<tr><td>UC2</td><td>Login</td><td>User</td><td>Valid password opens dashboard</td></tr>
<tr><td>UC3</td><td>Encrypt file</td><td>User</td><td>.fsm downloaded; ENCRYPT logged</td></tr>
<tr><td>UC4</td><td>Decrypt file</td><td>User</td><td>Original bytes returned; DECRYPT logged</td></tr>
<tr><td>UC5</td><td>Hash file</td><td>User</td><td>Digest shown; HASH logged</td></tr>
<tr><td>UC6</td><td>View log</td><td>User</td><td>Last 20 events listed</td></tr>
<tr><td>UC7</td><td>Logout</td><td>User</td><td>Session cleared</td></tr>
</table>

<h3>6.7 Database analysis</h3>
<p><strong>Table users:</strong> id (PK), username (unique), password_hash.</p>
<p><strong>Table logs:</strong> id (PK), username, action, filename, detail, created_at.</p>
<p>The schema is unnormalised beyond 1NF by design: it is an event list, not a warehouse. No foreign key to users is strictly required for the prototype; username is copied into the log for simple queries.</p>

<h3>6.8 Threats considered (defensive view)</h3>
<table>
<tr><th>Concern</th><th>Control in this mini project</th></tr>
<tr><td>Stolen laptop with .fsm files</td><td>AES-GCM; attacker lacks file password</td></tr>
<tr><td>Altered ciphertext</td><td>GCM authentication tag fails; decrypt refused</td></tr>
<tr><td>Altered ordinary file</td><td>SHA-256 mismatch against stored digest</td></tr>
<tr><td>Stolen database of login hashes</td><td>Werkzeug password hashes; still a residual risk if passwords are weak</td></tr>
<tr><td>Anonymous use of tools</td><td>Login required for dashboard routes</td></tr>
<tr><td>Very large upload exhausting memory</td><td>16 MB MAX_CONTENT_LENGTH</td></tr>
</table>
<p>The prototype is <strong>not</strong> claimed to be safe on the public Internet. Chapter 10 lists hardening steps if the work is extended.</p>

<div class="page-break"></div>
<h2>CHAPTER 7 &nbsp; TOOLS USED</h2>

<h3>7.1 Software tools</h3>
<table>
<tr><th>Layer</th><th>Tool / Technology</th><th>Version / note</th><th>Purpose</th></tr>
<tr><td>Language</td><td>Python</td><td>3.12 (typical)</td><td>Backend and crypto glue</td></tr>
<tr><td>Web framework</td><td>Flask</td><td>3.x</td><td>Routes, sessions, uploads</td></tr>
<tr><td>Crypto library</td><td>cryptography (PyCA)</td><td>43.x</td><td>AESGCM, PBKDF2HMAC</td></tr>
<tr><td>Hashing</td><td>hashlib</td><td>Standard library</td><td>SHA-256 of files</td></tr>
<tr><td>Password hashing</td><td>Werkzeug</td><td>Bundled with Flask</td><td>Login password storage</td></tr>
<tr><td>Database</td><td>SQLite</td><td>File fsm.db</td><td>Users and logs</td></tr>
<tr><td>Templates</td><td>Jinja2</td><td>With Flask</td><td>HTML rendering</td></tr>
<tr><td>Markup</td><td>HTML5</td><td>—</td><td>Structure</td></tr>
<tr><td>Styling</td><td>Tailwind CSS</td><td>CDN</td><td>Presentation</td></tr>
<tr><td>IDE</td><td>Cursor / VS Code</td><td>—</td><td>Editing</td></tr>
<tr><td>Browser</td><td>Chrome / Firefox / Edge</td><td>—</td><td>UI testing</td></tr>
<tr><td>OS</td><td>Linux (portable to Windows)</td><td>—</td><td>Host</td></tr>
<tr><td>VCS</td><td>Git</td><td>—</td><td>Source history</td></tr>
</table>

<h3>7.2 Hardware requirements (minimum)</h3>
<table>
<tr><th>Item</th><th>Specification</th></tr>
<tr><td>Processor</td><td>Any dual-core CPU, 1.5 GHz or above</td></tr>
<tr><td>Memory</td><td>4 GB RAM (8 GB recommended)</td></tr>
<tr><td>Disk</td><td>200 MB free for project, venv and sample files</td></tr>
<tr><td>Display</td><td>1366 × 768 or higher</td></tr>
<tr><td>Network</td><td>Not required at runtime except first load of Tailwind CDN</td></tr>
</table>

<h3>7.3 Justification of stack</h3>
<p>Python is the language most students of cyber security already use for scripting. Flask is a micro-framework: one file can hold the whole server, which is ideal for viva. Tailwind produces an acceptable UI without a large CSS codebase. SQLite needs no separate database server. The cryptography library wraps OpenSSL-quality primitives so the student does not invent AES.</p>

<div class="page-break"></div>
<h2>CHAPTER 8 &nbsp; SYSTEM DESIGN AND IMPLEMENTATION</h2>

<h3>8.1 Module description</h3>
<table>
<tr><th>Module</th><th>Functions / routes</th><th>Responsibility</th></tr>
<tr><td>Authentication</td><td>/register, /login, /logout</td><td>Account lifecycle and session</td></tr>
<tr><td>Encryption</td><td>/encrypt, encrypt_bytes()</td><td>PBKDF2 + AES-GCM + .fsm header</td></tr>
<tr><td>Decryption</td><td>/decrypt, decrypt_bytes()</td><td>Parse, authenticate, restore name</td></tr>
<tr><td>Integrity</td><td>/hash</td><td>SHA-256 and optional verify</td></tr>
<tr><td>Logging</td><td>add_log()</td><td>Insert into logs table</td></tr>
<tr><td>Presentation</td><td>templates/*.html</td><td>Forms and log table</td></tr>
</table>

<h3>8.2 Algorithm — key derivation (conceptual)</h3>
<pre>
Input:  password P, salt S (16 random bytes)
Output: 32-byte key K
K ← PBKDF2-HMAC-SHA256(P, S, iterations = 200000, dkLen = 32)
</pre>
<p>A unique salt per encryption means that two encryptions of the same file with the same password still produce different ciphertext.</p>

<h3>8.3 Algorithm — encrypt (conceptual)</h3>
<pre>
Input:  plaintext M, password P, original name N
S ← random 16 bytes
Nonce ← random 12 bytes
K ← PBKDF2(P, S)
C ← AES-256-GCM-Encrypt(K, Nonce, M)
return  "FSM1" || len(N) || N || S || Nonce || C
</pre>

<h3>8.4 Algorithm — decrypt (conceptual)</h3>
<pre>
Parse header; reject if magic ≠ "FSM1"
K ← PBKDF2(P, S)
M ← AES-256-GCM-Decrypt(K, Nonce, C)   // fails if tag invalid
return M and original name N
</pre>

<h3>8.5 User interface</h3>
<p><strong>Login page:</strong> username, password, link to register.</p>
<p><strong>Register page:</strong> create account.</p>
<p><strong>Dashboard:</strong> three cards (Encrypt, Decrypt, Hash) and a table of the last twenty log rows. The logged-in username and a Logout link appear in the header. Hash results, when present, appear in a panel above the log.</p>

<h3>8.6 Implementation notes</h3>
<ul>
<li>Flask <code>MAX_CONTENT_LENGTH</code> enforces the 16 MB cap.</li>
<li><code>secure_filename</code> is applied to names written on disk.</li>
<li>Decorator <code>login_required</code> protects encrypt, decrypt, hash and dashboard.</li>
<li>Database file lives in <code>instance/fsm.db</code> and is created automatically.</li>
<li>Temporary outputs are written under <code>uploads/</code> for download via <code>send_file</code>.</li>
</ul>

<h3>8.7 Screens (for viva)</h3>
<p>During demonstration the student should show: (1) registration, (2) failed login, (3) successful login, (4) encryption of a short text file, (5) opening the .fsm file in a text editor to show that it is not readable, (6) successful decrypt, (7) failed decrypt with a wrong password, (8) SHA-256 matching an independent tool, (9) log table containing ENCRYPT, DECRYPT, HASH and DECRYPT_FAIL.</p>

<div class="page-break"></div>
<h2>CHAPTER 9 &nbsp; TEST CASES</h2>
<p>Testing was performed as black-box validation against the functional requirements. Representative results are recorded below. Status “Pass” means the observed behaviour matched the expected result on the development machine.</p>
<table>
<tr><th>TC ID</th><th>Condition</th><th>Input</th><th>Expected result</th><th>Actual result</th><th>Status</th></tr>
<tr><td>TC01</td><td>New registration</td><td>Unique user + password</td><td>Account created; login page</td><td>Flash: account created</td><td>Pass</td></tr>
<tr><td>TC02</td><td>Duplicate user</td><td>Existing username</td><td>Error, no second account</td><td>Username already exists</td><td>Pass</td></tr>
<tr><td>TC03</td><td>Invalid login</td><td>Wrong password</td><td>Generic failure</td><td>Invalid username or password</td><td>Pass</td></tr>
<tr><td>TC04</td><td>Valid login</td><td>Correct credentials</td><td>Dashboard</td><td>Dashboard displayed</td><td>Pass</td></tr>
<tr><td>TC05</td><td>Encrypt incomplete</td><td>Missing file or password</td><td>Rejected</td><td>Error flash / HTML required</td><td>Pass</td></tr>
<tr><td>TC06</td><td>Encrypt sample</td><td>text file + password</td><td>.fsm with magic FSM1</td><td>Header FSM1 confirmed</td><td>Pass</td></tr>
<tr><td>TC07</td><td>Decrypt correct</td><td>.fsm + same password</td><td>Original bytes</td><td>Plaintext restored</td><td>Pass</td></tr>
<tr><td>TC08</td><td>Decrypt wrong password</td><td>.fsm + wrong password</td><td>No plaintext; log fail</td><td>DECRYPT_FAIL logged</td><td>Pass</td></tr>
<tr><td>TC09</td><td>SHA-256 known file</td><td>Sample file</td><td>Matches sha256sum</td><td>Digests identical</td><td>Pass</td></tr>
<tr><td>TC10</td><td>Hash match</td><td>File + correct expected</td><td>Match message</td><td>Match indicated</td><td>Pass</td></tr>
<tr><td>TC11</td><td>Hash mismatch</td><td>File + wrong expected</td><td>Tamper warning</td><td>Mismatch indicated</td><td>Pass</td></tr>
<tr><td>TC12</td><td>Activity log</td><td>After operations</td><td>Rows for each action</td><td>ENCRYPT/DECRYPT/HASH present</td><td>Pass</td></tr>
<tr><td>TC13</td><td>Authz</td><td>GET /dashboard logged out</td><td>Redirect to login</td><td>Redirected</td><td>Pass</td></tr>
<tr><td>TC14</td><td>Logout</td><td>Logout link</td><td>Session ended</td><td>Login shown</td><td>Pass</td></tr>
<tr><td>TC15</td><td>Size limit</td><td>File &gt; 16 MB</td><td>Request refused</td><td>Flask 413 / limit</td><td>Pass</td></tr>
</table>
<p>The examiner may repeat TC06 to TC09 as a live practical. A short text file (for example one line of ASCII) is sufficient and easy to verify by eye after decryption.</p>

<h2>CHAPTER 10 &nbsp; SECURITY RECOMMENDATIONS</h2>
<p>The following recommendations concern <strong>safe configuration and responsible use</strong> of this academic prototype. They do not provide attack procedures.</p>
<ol>
<li><strong>Choose a long file passphrase.</strong> PBKDF2 slows guessing but cannot save a two-word dictionary password.</li>
<li><strong>Keep the login password and the file password different.</strong></li>
<li><strong>Do not store the file password in the same folder as the .fsm file.</strong></li>
<li><strong>Change Flask’s default secret_key</strong> before any use outside the student’s own machine; supply it through an environment variable.</li>
<li><strong>Run the server on localhost only</strong> for this version. Do not port-forward it to the Internet.</li>
<li><strong>Use HTTPS</strong> if the application is ever placed on a college intranet, so that passwords are not sent in clear HTTP.</li>
<li><strong>Delete files in the uploads directory</strong> after a demo; decrypted output may remain there temporarily.</li>
<li><strong>Update Python packages</strong> when faculty policy allows, so that library defects can be patched.</li>
<li><strong>Remember that SHA-256 does not hide data.</strong> Hashing is not encryption.</li>
<li><strong>Back up .fsm files</strong>, and accept that a lost password means permanent loss of plaintext — that is the correct behaviour of encryption.</li>
<li><strong>Do not use this prototype to protect examination papers, medical data or production secrets</strong> until a later, hardened version is reviewed by faculty.</li>
<li><strong>Future production controls</strong> (not implemented here): account lockout, HTTPS, role-based access, hardware-backed keys, structured log export, and a written backup policy.</li>
</ol>

<div class="page-break"></div>
<h2>CHAPTER 11 &nbsp; PROJECT WORK SUMMARY (REPORT)</h2>
<table>
<tr><th>Item</th><th>Detail</th></tr>
<tr><td>Title</td><td>File Security Manager</td></tr>
<tr><td>Student</td><td>Ayten</td></tr>
<tr><td>Programme</td><td>B.Sc. (Cyber Security), SPPU 2024 Pattern</td></tr>
<tr><td>Class / Semester</td><td>S.Y. / III</td></tr>
<tr><td>Type</td><td>Mini Project — working prototype</td></tr>
<tr><td>Frontend</td><td>HTML, Tailwind CSS</td></tr>
<tr><td>Backend</td><td>Python, Flask</td></tr>
<tr><td>Security mechanisms</td><td>AES-256-GCM, PBKDF2, SHA-256, hashed login, session, audit log</td></tr>
</table>
<p><strong>Deliverables:</strong> source code (app.py and templates), requirements.txt, README, this report in PDF, and a live demonstration.</p>
<p><strong>Learning outcomes:</strong> the student can explain authenticated encryption versus hashing; can justify why a key is derived rather than used as a raw password; can show access control and logging as complementary controls; and can run a small full-stack cyber-security application.</p>
<p><strong>Limitations accepted:</strong> local deployment, 16 MB files, no password recovery, no multi-file archives, default development secret key unless the student changes it, Tailwind CDN dependency unless CSS is cached.</p>

<h2>CHAPTER 12 &nbsp; CONCLUSION</h2>
<p>The mini project <strong>File Security Manager</strong> has been designed, implemented and tested as a compact teaching system for file-oriented cyber security. Confidentiality is achieved with AES-256-GCM. Keys are derived with PBKDF2 and are not stored. Integrity of arbitrary files is checked with SHA-256, while integrity of ciphertext is checked by the GCM tag. Users must authenticate before using the tools, and an activity log records encrypt, decrypt and hash events, including failed decryption.</p>
<p>The work satisfies the spirit of the SPPU Semester–III Mini Project: it is implementable on a student computer, it uses standard algorithms that can be defended in viva, and it remains modest in size. It is not a commercial product, and that limitation is intentional. Within the stated scope, the objectives listed in Chapter 3 have been met.</p>

<h2>CHAPTER 13 &nbsp; FUTURE ENHANCEMENT</h2>
<ol>
<li>HTTPS deployment on a college intranet with a managed secret key.</li>
<li>Role-based access control (student, faculty, administrator) and log export.</li>
<li>Secure deletion (overwrite) of temporary plaintext after download.</li>
<li>Folder / multi-file encryption with a progress indicator and a higher size limit.</li>
<li>Optional key-file or hardware-token based unlocking in addition to a typed password.</li>
<li>Digital signatures (for example Ed25519) to prove origin as well as integrity.</li>
<li>Two-factor authentication for the web login.</li>
<li>Fully offline UI (vendored CSS) for laboratories without Internet.</li>
<li>Automated unit tests for header parsing and decrypt-failure paths.</li>
<li>A faculty-supervised configuration review before any data of real sensitivity is processed.</li>
</ol>

<div class="page-break"></div>
<h2>CHAPTER 14 &nbsp; BIBLIOGRAPHY</h2>
<p>The following books, standards and official documentation were consulted. Online documents were accessed during the academic year 2025–26.</p>
<p>[1] W. Stallings, <em>Cryptography and Network Security: Principles and Practice</em>, Pearson Education.</p>
<p>[2] B. Schneier, <em>Applied Cryptography</em>, John Wiley &amp; Sons.</p>
<p>[3] NIST, <em>Advanced Encryption Standard (AES)</em>, FIPS Publication 197, National Institute of Standards and Technology, Gaithersburg, MD.</p>
<p>[4] NIST, <em>Recommendation for Block Cipher Modes of Operation: Galois/Counter Mode (GCM) and GMAC</em>, Special Publication 800-38D.</p>
<p>[5] NIST, <em>Secure Hash Standard (SHS)</em>, FIPS Publication 180-4.</p>
<p>[6] NIST, <em>Recommendation for Password-Based Key Derivation</em>, Special Publication 800-132.</p>
<p>[7] B. Kaliski, <em>PKCS #5: Password-Based Cryptography Specification, Version 2.0</em>, RFC 2898, IETF.</p>
<p>[8] Pallets Projects, <em>Flask Documentation</em>, https://flask.palletsprojects.com/</p>
<p>[9] Python Cryptographic Authority, <em>cryptography library documentation</em>, https://cryptography.io/</p>
<p>[10] SQLite Development Team, <em>SQLite Documentation</em>, https://www.sqlite.org/docs.html</p>
<p>[11] Tailwind Labs, <em>Tailwind CSS Documentation</em>, https://tailwindcss.com/docs</p>
<p>[12] Savitribai Phule Pune University, <em>B.Sc. (Cyber Security) 2024 Pattern Syllabus</em>, Faculty of Science and Technology, Pune.</p>
<p>[13] NIST, <em>SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions</em>, FIPS 202 (background reading on hash design).</p>
<p>[14] ISO/IEC 27001, <em>Information security, cybersecurity and privacy protection — Information security management systems</em> (contextual reading on controls and logging).</p>

<h2>APPENDIX A &nbsp; PROJECT FILE STRUCTURE</h2>
<pre>
file-security-manager/
  app.py
  requirements.txt
  README.md
  SPPU_Mini_Project_Report.md
  File_Security_Manager_Mini_Project_Report.pdf
  templates/
    base.html
    login.html
    register.html
    dashboard.html
  docs/
    generate_report.py
  instance/                 (runtime: fsm.db)
  uploads/                  (temporary processed files)
  venv/                     (local Python environment)
</pre>

<h2>APPENDIX B &nbsp; HOW TO RUN THE PROJECT</h2>
<pre>
cd file-security-manager
python3 -m venv venv
source venv/bin/activate          (Windows: venv\\Scripts\\activate)
pip install -r requirements.txt
python app.py
</pre>
<p>Open a browser at <strong>http://127.0.0.1:5000</strong>. Register a username, log in, then use Encrypt, Decrypt and SHA-256 Hash. Keep the file password in memory; the server does not save it.</p>

<p class="center" style="margin-top:36pt;"><strong>— End of Report —</strong></p>
</body>
</html>
"""

HTML_PATH.write_text(HTML, encoding="utf-8")
print(f"Wrote {HTML_PATH}")
print(f"PDF target {PDF_PATH}")
