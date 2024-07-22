# Example script to demonstrate recovering passwords from B2.txt

# Assume we have the new mask or new method of masking
new_mask = bytes.fromhex(
    "your_new_predefined_20_byte_mask_in_hex"
)  # Replace with actual 20-byte mask in hex
database_file_v2 = "/mnt/data/B2.txt"

with open(database_file_v2, "r") as f:
    lines = f.readlines()

for line in lines:
    if line.startswith("id = "):
        parts = line.split(";")
        id = parts[0].split("=")[1].strip()
        mdp_store = parts[1].split("=")[1].strip()
        mdp_store = bytes.fromhex(mdp_store)
        password = xor_bytes(mdp_store, new_mask)
        print(f"User: {id}, Password (hex): {password.hex()}")
