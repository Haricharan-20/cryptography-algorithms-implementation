from cryptography.fernet import Fernet

print("=== AES Encryption and Decryption Demo ===")

key = Fernet.generate_key()
cipher = Fernet(key)

message = input("Enter a message to encrypt: ")

encrypted = cipher.encrypt(message.encode())
print("\nEncrypted Message:")
print(encrypted.decode())

decrypted = cipher.decrypt(encrypted)
print("\nDecrypted Message:")
print(decrypted.decode())
