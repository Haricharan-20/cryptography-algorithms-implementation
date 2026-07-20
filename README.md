# 🔐 Cryptography Algorithms Implementation

> A Cyber Security Internship Project demonstrating practical cryptographic techniques using Python.

## 📖 Overview

This project demonstrates three fundamental cryptographic techniques:

- 🔒 **AES-256-GCM** — Symmetric authenticated encryption
- 🔑 **RSA-2048** — Asymmetric public-key encryption
- #️⃣ **SHA-256** — Cryptographic hashing

The project provides simple Python implementations to understand how encryption, decryption, and hashing are used in cybersecurity.

## 🎯 Objective

The objective of this project is to understand and practically demonstrate how cryptographic algorithms help protect data, provide confidentiality, and verify data integrity.

## 🛠️ Technologies Used

- Python 3
- Cryptography Library
- hashlib
- Git
- GitHub

## 📂 Project Structure

```text
cryptography-algorithms-implementation/
├── aes.py
├── rsa_encryption.py
├── sha256_hash.py
├── requirements.txt
└── README.md
```

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Haricharan-20/cryptography-algorithms-implementation.git
cd cryptography-algorithms-implementation
```

Install the required dependency:

```bash
pip install -r requirements.txt
```

## 💻 How to Run

### 🔒 AES-256-GCM

```bash
python aes.py
```

AES uses a 256-bit key and GCM authenticated encryption to securely encrypt and decrypt data.

### 🔑 RSA-2048

```bash
python rsa_encryption.py
```

RSA demonstrates asymmetric cryptography using a public key for encryption and a private key for decryption with OAEP and SHA-256.

### #️⃣ SHA-256

```bash
python sha256_hash.py
```

SHA-256 converts input data into a fixed-length 256-bit cryptographic hash.

## ✅ Results

The project was successfully implemented and tested.

- AES-256-GCM successfully encrypted and decrypted sample data.
- RSA-2048 successfully performed public-key encryption and private-key decryption.
- SHA-256 successfully generated a cryptographic hash from input data.

## 🧠 Learning Outcomes

Through this project, I learned about:

- Symmetric and asymmetric cryptography
- AES authenticated encryption
- Public and private keys
- RSA encryption and decryption
- Cryptographic hashing
- SHA-256
- Keys and nonces in cryptography
- Practical cryptography using Python

## ⚠️ Security Note

This project is intended for educational purposes. Real-world cryptographic systems require secure key storage, proper key management, secure protocols, and carefully reviewed implementations.

## 👤 Author

**Haricharan-20**

Cyber Security Internship Project
