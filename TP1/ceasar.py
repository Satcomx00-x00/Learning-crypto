#!/usr/bin/env python3

ciphertext = "ha ydebbnaiajp lwn zaywhwca aop bwexha!"

# L = [] # empty list
# L.append('a') # append a to the list
# print(L[0]) # print fist element of L
# L.index('a') # position(s) of element 'a' in the list L
# len(L) # number of element in L
# type(L) # type of variable L
# c = a%b # c = a modulo (b)

# a.lower() # string method --> lowercase
# a.upper() # string method --> uppercase
# M = ''.join(L) # concatenate L element with '' in between

# alphabet constant for reference
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(key, plaintext):
    result = ""
    for char in plaintext:
        if char.isalpha():
            index = ALPHABET.index(char)
            shifted_index = (index + key) % 26
            result += ALPHABET[shifted_index]
        else:
            result += char
    return result

# def decrypt(key, ciphertext):
#     result = ""
#     for char in ciphertext:
#         if char.isalpha():
#             index = ALPHABET.index(char)
#             shifted_index = (index - key) % 26
#             result += ALPHABET[shifted_index]
#         else:
#             result += char
#     return result

def decrypt(key, ciphertext):
    return encrypt(-key, ciphertext)

def attack(ciphertext):
    for key in range(26):
        plaintext_attempt = decrypt(key, ciphertext)
        print(f"Key {key}: {plaintext_attempt}")

if __name__ == "__main__":
    plaintext = "bonjour"
    key = 3

    encrypted = encrypt(key, plaintext)
    print(f"Encrypted: {encrypted}")
    
    decrypted = decrypt(key, encrypted)
    print(f"Decrypted: {decrypted}")

    attack(ciphertext)
        
    enc = encrypt(23, "bonjour a vous")
    print(f"Custom Encrypted: {enc}")
    
    attack(enc)
