import hashlib

print("=== SHA-256 Hashing Demo ===")

message = input("Enter text to hash: ")

hash_value = hashlib.sha256(message.encode()).hexdigest()

print("\nOriginal Message:")
print(message)

print("\nSHA-256 Hash:")
print(hash_value)
