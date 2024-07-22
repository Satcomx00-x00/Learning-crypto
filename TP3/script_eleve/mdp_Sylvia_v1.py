import os 

DB = []
mask = os.urandom(20)


def add_user(DB,id, mdp):
    if len(mdp)!=20:
        print("Longueur mot de passe incorrecte")
        exit()
    if id in DB :
        print("Utilisateur déjà existant")
    mdp_store = bytes(a ^ b for (a, b) in zip(mask, mdp)) 
    DB.append((id, mdp_store))
    return DB

#première base de données
DB = add_user(DB,"mrc" , b"HDY64!MJGFDT3ZSGzert")
# DB = add_user(DB,"titi1234", b'***')
# DB = add_user(DB,"viveBali", b'***')
# DB = add_user(DB,"Thibaut",  b'***')
# DB = add_user(DB,"Mallory",  b'***')
# DB = add_user(DB,"Fandu92",  b'***')


#Affichage
# print(DB)

# for element in DB : 
#     print("id = {}; mdp_store = {}".format(element[0],element[1].hex()))



