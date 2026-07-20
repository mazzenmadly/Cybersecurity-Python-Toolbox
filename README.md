
# Cybersecurity Python Toolbox 🛡️

A comprehensive suite of Python-based security tools designed for secure identity verification, password security enhancement, and file operations.

---

## 📂 Project Structure

*   **`Identity-Access-Management/`**: Implements secure user authentication mechanics using a local Master Key verified via SHA-256.
*   **`Password-Security-Suite/`**: Tools for strong password generation and evaluating password complexity/strength metrics.
*   **`Cryptography-File-Security/`**: Focuses on data integrity and secure file operations.

---

## 🛠️ Security Practices Applied
*   **Password Hashing:** Utilizing secure algorithms (`SHA-256`) rather than plain-text storage.
*   **Privacy Control:** Incorporating `.gitignore` to prevent sensitive application state files (like `master_key.txt`) from being exposed publicly.
