# -*- coding: utf-8 -*-
"""
@authors: Cyril Génisson
@file: chiffre.py

@project: Colibri
@licence: GPLv3
"""
from math import gcd

def cesar(chaine, decal, option):
    '''Code une chaîne de caractère avec le chiffre de César augmenté
        sur toute la table ASCII:
            -chaine: chaîne de caractère de la table ASCII
            -decal: lettre de décalage
            -option: 'c' ou 'd' pour chiffrer ou déchiffrer
    '''
    sortie = ''
    if option == 'c':
        for k in range(0, len(chaine)):
            sortie += chr((ord(chaine[k]) + ord(decal)) % 256)
        return sortie
    else:
        for k in range(len(chaine)):
            sortie += chr((ord(chaine[k]) - ord(decal)) % 256)
        return sortie


def vigenere(chaine, clef, option):
    '''Code une chaîne de carctère avec le chiffre de Vigenère augmenté
        sur toute la table ASCII:
            -chaine: chaîne de caractère de la table ASCII
            -clef: chaîne de caractère secrète
            -option: 'c' ou 'd' pour chiffrer ou déchiffrer
    '''
    sortie = ''
    key = clef
    # On met la clef à la bonne dimension par rapport au message
    for k in range(len(chaine) // len(key)):
        key += clef
    for k in range(len(chaine)):
        sortie += cesar(chaine[k], key[k], option)
    return sortie


def inverse(a):
    '''Calcul l'inverse d'un nombre a modulo 256. Utile pour le chiffrement
        affine.
    '''
    x = 0
    while ((a * x) % 256 != 1):
        x = x + 1
    return x


def affine(chaine, a, b, option):
    '''Code une chaîne de caractère à l'aide d'un chiffremenet affine:
        -chaine: chaine de caractère de la table ASCII
        -a: un entier permier avec 256
        -b; un entier
        -option: 'c' ou 'd' pour chiffrer ou déchiffrer
    '''
    sortie = ''
    if gcd(a, 256) != 1:
        print("Le nombre, ", a, " doit être permier avec 256.")
        return "Erreur"
    if option == 'c':
        for k in range(len(chaine)):
            sortie += chr((a*ord(chaine[k]) + b) % 256)
        return sortie
    else:
        for k in range(len(chaine)):
            sortie += chr(inverse(a) * (ord(chaine[k]) - b) % 256)
        return sortie
