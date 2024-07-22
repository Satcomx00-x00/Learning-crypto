mask = b'your_predefined_20_byte_mask'  # This should be the mask used in the XOR operation
database_file = 'B1.txt'


def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


with open(database_file, "r") as f:
    lines = f.readlines()

for line in lines:
    if line.startswith("id = "):
        parts = line.split(";")
        id = parts[0].split("=")[1].strip()
        mdp_store = parts[1].split("=")[1].strip()
        mdp_store = bytes.fromhex(mdp_store)
        password = xor_bytes(mdp_store, mask)
        print(f"User: {id}, Password (hex): {password.hex()}")
