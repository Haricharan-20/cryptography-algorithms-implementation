# Cryptography Algorithms Implementation

## Cyber Security Internship Project

This project demonstrates three fundamental cryptographic techniques using Python: AES-256 encryption, RSA-2048 encryption, and SHA-256 hashing.

## Objective

The objective of this project is to understand and practically demonstrate how cryptographic algorithms are used to protect data, provide confidentiality, and verify data integrity.

## Algorithms Implemented

### 1. AES-256-GCM
AES is a symmetric encryption algorithm where the same secret key is used for encryption and decryption.

This project uses:
- 256-bit AES key
- GCM authenticated encryption mode
- Random 12-byte nonce

File: `aes.py`

### 2. RSA-2048
RSA is an asymmetric cryptographic algorithm that uses two keys:
- Public key for encryption
- Private key for decryption

This implementation uses a 2048-bit RSA key with OAEP padding and SHA-256.

File: `rsa_encryption.py`

### 3. SHA-256
SHA-256 is a cryptographic hash function that converts input data into a fixed 256-bit hash value.

Unlike encryption, hashing is a one-way process and is commonly used for integrity verification and secure password-storage systems when combined with appropriate password-hashing techniques.

File: `sha256_hash.py`

## Technologies Used

- Python 3
- Cryptography Python library
- hashlib
- Termux on Android
- Git and GitHub

## Project Structure

cryptography-algorithms-implementation/
├── aes.py
├── rsa_encryption.py
├── sha256_hash.py
├── requirements.txt
└── README.md

## Installation

Install the required dependency:

pip install -r requirements.txt

## How to Run

AES-256:

python aes.py

RSA-2048:

python rsa_encryption.py

SHA-256:

python sha256_hash.py

## Results

The project was successfully tested with sample text.

- AES-256-GCM successfully encrypted and decrypted the original message.
- RSA-2048 successfully performed public-key encryption and private-key decryption.
- SHA-256 successfully generated a 256-bit cryptographic hash.

## Learning Outcomes

Through this project, I learned:

- Symmetric and asymmetric cryptography
- AES encryption and authenticated encryption
- Public and private key concepts
- RSA encryption
- Cryptographic hashing
- SHA-256
- Importance of keys and nonces in cryptography
- Practical implementation of cryptography using Python

## Security Note

This project is intended for educational demonstration. Real-world cryptographic systems require secure key storage, proper key management, secure protocols, and carefully reviewed implementations.

## Author

Haricharan-20

## Disclaimer

This project was developed for educational purposes as part of a Cyber Security Internship.
