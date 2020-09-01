# -*- coding: utf-8 -*-
"""
@authors: Cyril Génisson
@file: fonctions.py

@project: Colibri
@licence: GPLv3
"""


def parite(x):
    '''Renvoie True si le nombre est pair.'''
    if x % 2:
        return False
    else:
        return True


def car2bin(car):
    '''Renvoie la valeur binaire d'un caractère de la table ASCII.'''
    return(bin(ord(car))[2:].zfill(8))


def bin2int(octet):
    '''Convertie un octet en entier.'''
    entier = 0
    for k in range(len(octet)):
        if octet[k] == '1':
            entier += 2**(7-k)
    return entier


def text2bin(chaine):
    '''Convertie une chaîne de caractère de la table ASCII
    en chane bianire.'''
    binaire = ''
    for k in range(len(chaine)):
        binaire += car2bin(chaine[k])
    return binaire


def bin2text(binaire):
    '''Convertie une chaîne binaire en une suite de caractères'''
    text = ''
    for k in range(len(binaire)//8):
        text += chr(bin2int(binaire[8*k:8*(k+1)]))
    return text


def menu_chiffre():
    print()
    print("*****************************")
    print("* Algorithme de chiffrement *")
    print("*****************************")
    print()
    print("1: Vigenère")
    print("2: Affine")
    print("3: César ")
    print("4: Sans chiffre")
    print


def menu_main():
    print("*********************************")
    print("* Stéganographie et chiffrement *")
    print("*********************************")
    print
    print("1: Protection de l'information")
    print("2: Récupération de l'information")
    print


def menu_stego():
    print("***************************")
    print("* Stéganographie d'images *")
    print("***************************")
    print
    print("1: Protection de l'image")
    print("2: Récupération de l'image")
    print