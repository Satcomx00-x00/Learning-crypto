import hmac
import hashlib

message = b"message"
key = b"key_16_bytes_long"


def calculate_hmac(key, message, hash_function):
    return hmac.new(key, message, hash_function).hexdigest()


hmac_sha224 = calculate_hmac(key, message, hashlib.sha224)
hmac_sha256 = calculate_hmac(key, message, hashlib.sha256)
hmac_sha384 = calculate_hmac(key, message, hashlib.sha384)
hmac_sha512 = calculate_hmac(key, message, hashlib.sha512)

print(f"HMAC-SHA-224: {hmac_sha224}")
print(f"HMAC-SHA-256: {hmac_sha256}")
print(f"HMAC-SHA-384: {hmac_sha384}")
print(f"HMAC-SHA-512: {hmac_sha512}")

# Observation: résultats différents pour différentes fonctions de hachage
# --------------------------------------------
# Define different keys
key_16_bytes = b"key_16_bytes_long"  # 128-bit key
key_24_bytes = b"key_24_bytes_longer"  # 192-bit key
key_32_bytes = b"key_32_bytes_longest"  # 256-bit key


# Function to calculate HMAC-SHA-256 with different key sizes
def calculate_hmac_sha256(key, message):
    return hmac.new(key, message, hashlib.sha256).hexdigest()


# Calculate HMAC-SHA-256 with different key sizes
hmac_sha256_16 = calculate_hmac_sha256(key_16_bytes, message)
hmac_sha256_24 = calculate_hmac_sha256(key_24_bytes, message)
hmac_sha256_32 = calculate_hmac_sha256(key_32_bytes, message)

print(f"HMAC-SHA-256 with 128-bit key: {hmac_sha256_16}")
print(f"HMAC-SHA-256 with 192-bit key: {hmac_sha256_24}")
print(f"HMAC-SHA-256 with 256-bit key: {hmac_sha256_32}")

# Observation: La longueur de sortie reste la même, mais la taille de la clé affecte la sécurité
# --------------------------------------------
import os

key = os.urandom(32)  # 32 bytes = 256 bits


def calculate_hmac_sha256(key, message):
    return hmac.new(key, message, hashlib.sha256).hexdigest()


message = b"This is a test message."
tag = calculate_hmac_sha256(key, message)

print(f"Shared key: {key.hex()}")
print(f"Message: {message}")
print(f"Tag: {tag}")


def verify_hmac_sha256(key, message, tag):
    calculated_tag = calculate_hmac_sha256(key, message)
    return hmac.compare_digest(calculated_tag, tag)


is_valid = verify_hmac_sha256(key, message, tag)
print(f"Is the message valid? {is_valid}")
