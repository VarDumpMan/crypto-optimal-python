# coding:utf-8

def crypt_char(char, key):

    if char.isalpha():
        lettre1 = "a"

        key = key.upper()

        if (ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 65 and ord(char) <= 90):
            if char.islower():
                lettre1 = lettre1.lower()
            else:
                lettre1 = lettre1.upper()

            equivalente_ascii = ( ( ord(char) - ord(lettre1) + ord(key) - ord("A") ) % 26 ) + ord(lettre1)
        
            return chr(equivalente_ascii)
        else:
            return False
    else:
        return char

def crypt_string(string, key):
    i = 0
    equivalente = ""
    while i<len(string):
        sous_bloc = string[i:i+len(key)]
        
        j = 0
        for lettre in sous_bloc:
            if crypt_char(lettre, key[j]) is not False:
                equivalente += crypt_char(lettre, key[j])
            else:
                return False
            j+=1
        
        i+= len(key)
        
    return equivalente