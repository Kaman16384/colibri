#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# ATTENTION:
#   * LE CARACTERE DE TERMINAISON DE LA SEQUENCE BINAIRE EST: 1111111111111111
#
from PIL import Image

# Fonction d'encodage 
def CodageVigenere(text, key):
	crypt=""
	lenkey=""
	# Mets la clef à la bonne dimension
	for k in range(0, len(text)):
		lenkey += key
	# Crypte le message
	for k in range(0, len(text)):
		crypt += chr((ord(text[k]) + ord(lenkey[k]))% 256)
	return crypt

# Fonction de décodage
def DecodageVigenere(crypt, key):
	text=""
	lenkey=""
	# Mets la cle à la bonne dimension
	for k in range(0, len(crypt)):
		lenkey += key
	# Decrypte le message
	for k in range(0, len(crypt)):
		text += chr((ord(crypt[k]) - ord(lenkey[k]))%256)
	return text

# Fonction convertissant une chaîne de caractères en binaire sur 1 octet
# et retourne la chaîne binaire correspondante.
def TextToBin(chaine):
    binaire=""
    for k in range(len(chaine)):
        binaire += bin(ord(chaine[k]))[2:].zfill(8)
    binaire += '1111111111111111'
    return binaire

# Fonction BinToInt: convertis un binaire 8 bits en entier
def BinToInt(chaine):
	entier = 0
	for k in range(len(chaine)):
	        if  chaine[k] == '1':
        	    entier += 2**(7-k)
    	return entier

# Fonction convertissant une chaine de caratères binaire en caractère ASCII
def BinToText(chaine):
    	taille = len(chaine)
    	texte=''
    	for k in range(len(chaine)//8):
        	bit = chaine[8*k:taille-8]
        	texte +=  chr(int(BinToInt(bit)))
    	return texte

# Fonction de test de parité.
# Retourne True si le nombre est pair et False sinon.
def TestParite(number):
    parite = True
    if (number%2):
        parite = False
    return parite

# Fonction d'ouverture d'image et retourne le tableau de l'image associé.
def OpenPict(picture):
    pict = Image.open(picture)
    array = list(pict.getdata())
    return array

def Dimension(picture):
    pict = Image.open(picture)
    return pict.size

# Fonction d'encodage d'une image à partir d'un tableau.
def EncodePict(array, nl, nc, file_save):
    print("Encodage de l'image: " + CODE)
    img=Image.new("L", (nl,nc))
    img.putdata(array)
    img.save(file_save)

# Fonction d'encodage stéganographique d'un message.
def stegano(string, picture):
    array = OpenPict(picture)
    nc, nl= Dimension(picture)
    binaire = TextToBin(string)
    for k in range(len(binaire)):
        if binaire[k] == '1':
            if TestParite(array[k]):
                array[k] += 1
        else:
            if TestParite(array[k])== False:
                array[k] -= 1
    EncodePict(array, nc, nl, CODE)
    print("L'information secrète est codée dans la nouvelle image :-)")

# Fonction de décodage stéganographique
def unstegano(picture):
	array = OpenPict(picture)
    	message = ''
    	for k in range(len(array)):
        	if TestParite(array[k]):
	            	message += '0'
        	else:
        	    	message += '1'
        	if message[len(message)-16:] == '1111111111111111':
            		break
    	return BinToText(message[:-16])

IMAGE=""
KEY=""
fichier=""
CODE="Code.png"
END="Fin du programme. ENJOY"

def menu():
	print("*********************************")
	print("* Stéganographie et chiffrement *")
    	print("*********************************")
	print
	print("1: Protection de l'information")
	print("2: Récupération de l'information")
	print
	choix = int(input("Entrez votre choix: "))
	if choix == 1:
		IMAGE = raw_input("Nom de l'image à utiliser: ")
		KEY = raw_input("Clef de crytage à utiliser: ")
		filename = raw_input("Nom du fichier à camoufler: ")
		fichier = open(filename, "r")
		SECRET = fichier.read()
		fichier.close()
		print("Crytage de l'information par la méthode Vigenère améliorée:")
		stegano(CodageVigenere(SECRET,KEY),IMAGE)
		print("Le message est codé dans le fichier image Code.png")
		print(END)
	elif choix == 2:
		IMAGE = raw_input("Nom de l'image à analyser: ")
		KEY = raw_input("Clef de décryptage: ")
		print((DecodageVigenere(unstegano(IMAGE),KEY)))
		print(END)
		
	else:
		print("Help: pour utiliser se programme utiliser les choix: 1 ou 2")
		print(END)

# Lancement du programme
menu()
