from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


# variable de type byte 'immutable' (ne peut être modifiée). Il s'agit d'un tableau d'octets.
a = b'toto'

#variable de type bytearray (modifiable)
b = bytearray(b'toto')
print(b[0]) 

print("longueur ", len(b))
print("valeur de b encodé : ", b)
print("valeur de b en héxa : ", b.hex())

#Remplir un bytearray à partir de valeur hexa directement
c = bytearray.fromhex("0178be45")

# padding 
# plaintext_padde = pad(plaintext_unpad, AES.block_size, style = 'iso7816')
# cipher = AES.new(key, AES.MODE_ECB) ensuite ciphertext = cipher.encrypt(plaintext)
# r = get_random_bytes(22) #génération de 22 octets aléatoires
# c[0:16] #affichage des octets entre 0 et 16 du bytearray c

