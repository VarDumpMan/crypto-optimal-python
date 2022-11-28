# coding:utf-8

from modules.functions import crypt_string

texte = input("Entrer le texte en clair : ")
cle = input("Entrer la clé : ")

if crypt_string(texte, cle) is False:
    print('Pas de caractères spéciaux !')
else:
    print("La forme cryptée est : " + crypt_string(texte, cle))
