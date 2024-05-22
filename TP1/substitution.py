#!/usr/bin/env python3
# Substitution

# Écrire une fonction substitution qui va remplacer chaque lettre de l’alphabet par
# une autre (les caractères spéciaux restent inchangés pour faciliter l’implémentation). Elle prendra en entrée, les deux alphabets en question. Quelle est la clé de
# chiffrement dans ce cas ?
# Page 1 of 2 Louiza Khati
# Cryptographie TP 1
# 2. Réfléchir à un point faible de cette méthode de chiffrement vu en cours. Implémenter
# une attaque grâce à cette faiblesse et retrouver le clair correspondant à la variable
# ciphertext dans le fichier substitution.py. (Pour rappels, les caractères spéciaux
# ne sont pas chiffrés).
# 3. Choisissez une substitution et chiffrer un texte secret. Donnez le chiffré à un camarade pour qu’il tente de l’attaquer. De même, vous recevrez un chiffré, essayez de
# retrouver le clair. Que constatez-vous ?
# 4. Bonus Pour aller plus loin : Enrichir les fonctions pour détecter les erreurs : par
# exemple, si le type des entrées des fonctions n’est pas correcte, etc. . ..


ciphertext = "oz hlggrhv, o'viivfi, ov kvxsv, oz ovhrmv,lxxfkvmg mlh vhkirgh\
vg gizezroovmg mlh xlikh,vg mlfh zornvmglmh mlh zrnzyovh ivnliwh,xlnnv ovh\
 nvmwrzmgh mlfiirhhvmg ovfi evinrmv.mlh kvxsvh hlmg gvgfh, mlh ivkvmgrih hlmg\
 ozxsvh ;mlfh mlfh uzrhlmh kzbvi tizhhvnvmg mlh zevfc,vg mlfh ivmgilmh tzrvnvmg\
 wzmh ov xsvnrm ylfiyvfc,xilbzmg kzi wv eroh kovfih ozevi glfgvh mlh gzxsvh.hfi\
 o’livroovi wf nzo x'vhg hzgzm girhnvtrhgvjfr yvixv olmtfvnvmg mlgiv vhkirg vmxszmgv,\
 vg ov irxsv nvgzo wv mlgiv elolmgvvhg glfg ezklirhv kzi xv hzezmg xsrnrhgv.x’vhg ov\
 wrzyov jfr grvmg ovh uroh jfr mlfh ivnfvmg !zfc lyqvgh ivkftmzmgh mlfh gilfelmh wvh zkkzh ;\
 xszjfv qlfi evih o’vmuvi mlfh wvhxvmwlmh w’fm kzh,hzmh sliivfi, z gizevih wvh gvmvyivh jfr kfvmg.\
 zrmhr jf’fm wvyzfxsv kzfeiv jfr yzrhv vg nzmtvov hvrm nzigbirhv w’fmv zmgrjfv xzgrm,mlfh elolmh zf \
 kzhhztv fm kozrhri xozmwvhgrmjfv mlfh kivhhlmh yrvm ulig xlnnv fmv ervroov lizmtv.hviiv, ulfinroozmg, \
 xlnnv fm nroorlm w’svonrmgsvh,wzmh mlh xvievzfc irylgv fm kvfkov wv wvnlmh,vg, jfzmw mlfh ivhkrilmh, \
 oz nlig wzmh mlh klfnlmhwvhxvmw, uovfev rmerhryov, zevx wv hlfiwvh kozrmgvh.hr ov erlo, ov klrhlm, ov klrtmziw, \
 o’rmxvmwrv,m’lmg kzh vmxli yilwv wv ovfih kozrhzmgh wvhhrmhov xzmvezh yzmzo wv mlh krgvfc wvhgrmh"

french = {'a': 0.06679764243614932, 'b': 0.0137524557956778, 'c': 0.029469548133595286, 'd': 0.03143418467583497, 'e': 0.14833005893909626, 'f': 0.005893909626719057, 'g': 0.008840864440078585, 'h': 0.012770137524557957, 'i': 0.0618860510805501, 'j': 0.0019646365422396855, 'k': 0.0, 'l': 0.05304518664047151, 'm': 0.0275049115913556, 'n': 0.10117878192534381, 'o': 0.06974459724950884, 'p': 0.030451866404715127, 'q': 0.009823182711198428, 'r': 0.06483300589390963, 's': 0.11100196463654224, 't': 0.06581532416502947, 'u': 0.05795677799607073, 'v': 0.019646365422396856, 'w': 0.0, 'x': 0.004911591355599214, 'y': 0.0029469548133595285, 'z': 0.0}

alphabet = 'abcdefghijklmnopqrstuvwxyz'
other_alphabet = 'zyxwvutsrqponmlkjihgfedcba'

def substitution (alphabet_in, alphabet_out, plaintext):
    result = ""
    for char in plaintext:
        if char.isalpha():
            index = alphabet_in.index(char)
            result += alphabet_out[index]
        else:
            result += char
    return result

def attack():
    for key in range(26):
        plaintext_attempt = substitution(other_alphabet, alphabet, ciphertext)
        print(f"Key {key}: {plaintext_attempt}")

if __name__ == "__main__":
    attack()
    