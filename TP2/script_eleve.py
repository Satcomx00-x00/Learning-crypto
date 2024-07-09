from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import binascii

# 1. Il est nécessaire de "padder" un message pour que sa longueur soit un multiple de la taille de bloc du chiffrement, ici 16 octets pour AES.
# 2. Le padding doit être réversible et univoque pour permettre un déchiffrement sans ambiguïté.

# variable de type byte 'immutable' (ne peut être modifiée). Il s'agit d'un tableau d'octets.
a = b'toto'

# variable de type bytearray (modifiable)
b = bytearray(b'toto')
print(b[0]) 

print("longueur ", len(b))
print("valeur de b encodé : ", b)
print("valeur de b en héxa : ", b.hex())

# Remplir un bytearray à partir de valeur hexa directement
c = bytearray.fromhex("0178be45")

# 3. Définir la variable plaintext de type byte
plaintext = b'toto' 

# 4. Utiliser les trois paddings suivants
padded_x923 = pad(plaintext, AES.block_size, style='x923') # padder avec des 0 et un octet de longueur à la fin
padded_iso7816 = pad(plaintext, AES.block_size, style='iso7816') # padder avec un 80 (hex) suivi de 00 jusqu'à la longueur nécessaire
padded_pkcs7 = pad(plaintext, AES.block_size, style='pkcs7') # padder avec des octets ayant pour valeur la longueur du padding

# 5. Afficher le résultat
print("Padded with x923:", binascii.hexlify(padded_x923))
print("Padded with iso7816:", binascii.hexlify(padded_iso7816))
print("Padded with pkcs7:", binascii.hexlify(padded_pkcs7))

# 6. Définir la variable full de type byte
full = b'totototototototo'
padded_full = pad(full, AES.block_size, style='pkcs7')
print("Full padded with pkcs7:", binascii.hexlify(padded_full))

# Le padding pkcs7 ajoute un bloc complet de padding lorsque le message est déjà un multiple de la taille du bloc

# 7. Fonction AES_encrypt_ECB
def AES_encrypt_ECB(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = pad(plaintext, AES.block_size, style='pkcs7')
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

# 8. Fonction AES_decrypt_ECB
def AES_decrypt_ECB(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext, AES.block_size, style='pkcs7')
    return plaintext

# 9. Tester les fonctions en chiffrant et déchiffrant des messages
key = get_random_bytes(16)
plaintext = b"Test message for ECB mode"
ciphertext = AES_encrypt_ECB(key, plaintext)
print("Ciphertext:", binascii.hexlify(ciphertext))
decrypted_text = AES_decrypt_ECB(key, ciphertext)
print("Decrypted text:", decrypted_text)

# 10. Essayer de chiffrer des messages avec des clés de tailles différentes
keys = [
    get_random_bytes(15),
    get_random_bytes(16),
    get_random_bytes(24),
    get_random_bytes(32),
    get_random_bytes(64)
]

plaintext = b"Test message for different key sizes"

for i, key in enumerate(keys):
    try:
        ciphertext = AES_encrypt_ECB(key, plaintext)
        decrypted_text = AES_decrypt_ECB(key, ciphertext)
        print(f"Key size {len(key)} bytes - Ciphertext: {binascii.hexlify(ciphertext)}")
        print(f"Key size {len(key)} bytes - Decrypted text: {decrypted_text}")
    except Exception as e:
        print(f"Key size {len(key)} bytes - Error: {str(e)}")

# 11. Chiffrer le mot m_1 = b’aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaa’
m_1 = b'aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaa'
key = get_random_bytes(16)
ciphertext_m1 = AES_encrypt_ECB(key, m_1)
print("Ciphertext m_1:", binascii.hexlify(ciphertext_m1))
