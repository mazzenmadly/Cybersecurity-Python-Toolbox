# Cybersecurity Python Toolbox 🛡️

A comprehensive suite of Python-based security tools designed for secure identity verification, cryptographic operations, and password security enhancement.

---

## 📂 Project Structure

*   **`Identity-Access-Management/`**: Implements secure user authentication mechanics using a local Master Key verified via SHA-256.
*   **`Cryptography-File-Security/`**: Focuses on data integrity and secure file operations.
    *   `caesar_cipher.py`: Implements classic two-way encryption and decryption for secure communication.
    *   `encryption.py`: Handles fundamental cryptographic hashing logic.
*   **`Password-Security-Suite/`**: Tools for managing and evaluating credential security.
    *   `b1_pass generator.py`: Generates randomized strong passwords.
    *   `b2_pass rate.py`: Evaluates password compliance and strength metrics.
    *   `word_shortener.py`: An obfuscation tool that converts strings into obscure shorthand codes.

---

## 🛠️ Security Practices Applied
*   **Two-Way Encryption:** Utilizing classic cryptography algorithms to secure text strings with dynamic shifting.
*   **Password Hashing:** Utilizing secure algorithms (`SHA-256`) rather than plain-text storage.
*   **Privacy Control:** Incorporating `.gitignore` to prevent sensitive application state files (like `master_key.txt`) from being exposed publicly.
