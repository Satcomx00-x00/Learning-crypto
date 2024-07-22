m_1 = b"tito"
m_2 = b"titn"

print(f"Type of m_1: {type(m_1)}")
print(f"Type of m_2: {type(m_2)}")
print(f"Hexadecimal value of m_1: {m_1.hex()}")
print(f"Hexadecimal value of m_2: {m_2.hex()}")

# --------------------------------------------
def xor(bytearray1, bytearray2):
    if len(bytearray1) != len(bytearray2):
        return "Error: Input bytearrays must have the same length"
    return bytearray(x ^ y for x, y in zip(bytearray1, bytearray2))


m_1_bytearray = bytearray(m_1)
m_2_bytearray = bytearray(m_2)
v = xor(m_1_bytearray, m_2_bytearray)
print(f"XOR result in hex: {v.hex() if isinstance(v, bytearray) else v}")

# --------------------------------------------
from Crypto.Hash import SHA256

hash_1 = SHA256.new(m_1).hexdigest()
hash_2 = SHA256.new(m_2).hexdigest()

print(f"SHA256 hash of m_1: {hash_1}")
print(f"SHA256 hash of m_2: {hash_2}")

assert hash_1 == "504db5aeeabd937a18a36b62d6e948d236b889b33c84e9e0561d7fda1c145bce"
assert hash_2 == "9734a6725a8cfd2f438aa871f4c1bf083e3bfc4b1d97bbb1a9e43220390abbdc"


# --------------------------------------------
hash_1_bytes = bytes.fromhex(hash_1)
hash_2_bytes = bytes.fromhex(hash_2)

print(f"Size of hash_1 in bits: {len(hash_1_bytes) * 8}")
print(f"Size of hash_2 in bits: {len(hash_2_bytes) * 8}")


difference = sum(x != y for x, y in zip(hash_1_bytes, hash_2_bytes))
print(f"Difference between hash_1 and hash_2: {difference} bytes differ.")
