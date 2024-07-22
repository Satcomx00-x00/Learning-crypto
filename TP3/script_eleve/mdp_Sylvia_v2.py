import os 

mask = os.urandom(19)

def add_user(DB,index, id, mdp):
    if len(mdp)!=20:
        print("Longueur mot de passe incorrecte")
        exit()
    if id in DB :
        print("Utilisateur déjà existant")     
        exit()  
    new_mask = index.to_bytes(1, 'big') + mask    
    print("mask utilisateur ", index," = ", new_mask.hex())
    mdp_store = bytes(a ^ b for (a, b) in zip(new_mask, mdp)) 
    DB.append((id, mdp_store))
    index = index +1
    return index, DB

#première base de données #changer les mots de passe
print("mask initial = ", mask.hex())
DB = []

# (index,DB) = add_user(DB,index,"travelplaya",       b'***')
# (index,DB) = add_user(DB,index,"photographer75",    b'***')
# (index,DB) = add_user(DB,index,"Nadiasoleil",       b'***')
# (index,DB) = add_user(DB,index,"Lechatorange",      b'***')

# Affichage
# for element in DB : 
#     print("id = {}; mdp_store = {}".format(element[0],element[1].hex()))
