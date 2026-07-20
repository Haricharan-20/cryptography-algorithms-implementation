from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

print("=== AES-256 Encryption and Decryption Demo ===")

# Generate a random 256-bit AES key
key = AESGCM.generate_key(bit_length=256)
aes = AESGCM(key)

# Generate a unique 12-byte nonce
nonce = os.urandom(12)

message = input("Enter a message to encrypt: ").encode()

# Encrypt the message
encrypted = aes.encrypt(nonce, message, None)

print("\nEncrypted Message:")
print(encrypted.hex())

# Decrypt the message
decrypted = aes.decrypt(nonce, encrypted, None)

print("\nDecrypted Message:")
print(decrypted.decode())
