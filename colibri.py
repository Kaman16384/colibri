# -*- coding: utf-8 -*-
"""
@authors: Cyril Génisson
@file: colibri.py

@project: Colibri
@licence: GPLv3
"""
import chiffre as cf
import stegano as st
import fonctions as fc

CODE = "Pictures/CODE.png"
RECOVERY = "Pictures/RECOVERY.png"
END = "Terminé"


def stego_message():
    fc.menu_main()
    choix = input("Entrez votre choix: ")
    if choix == '1':
        IMAGE = input("Nom de l'image à utiliser: ")
        filename = input("Nom du fichier texte à dissimuler: ")
        fichier = open(filename, "r")
        SECRET = fichier.read()
        fichier.close()
        fc.menu_chiffre()
        chiffre = input("Choix du chiffrement: ")
        if chiffre == '1':
            KEY = input("clef de chiffrement: ")
            st.stegano(IMAGE, cf.vigenere(SECRET, KEY, 'c'), CODE)
        elif chiffre == '2':
            X = int(input("Choisir un entier premier avec 256: "))
            Y = int(input("Choisir un entier: "))
            st.stegano(IMAGE, cf.affine(SECRET, X, Y, 'c'), CODE)
        elif chiffre == '3':
            X = input("Choisir une lettre du clavier: ")
            st.stegano(IMAGE, cf.cesar(SECRET, X, 'c'), CODE)
        else:
            st.stegano(IMAGE, SECRET, CODE)
        print("Le message est codé dans l'image")

    elif choix == '2':
        IMAGE = input("Nom de l'image à analyser: ")
        fc.menu_chiffre()
        chiffre = input("Choix du chiffrement: ")
        if chiffre == '1':
            KEY = input("Clef de décryptage: ")
            print((cf.vigenere(st.unstegano(IMAGE), KEY, 'd')))
        elif chiffre == '2':
            X = int(input("Choisir un entier premier avec 256: "))
            Y = int(input("Choisir un entier: "))
            print((cf.affine(st.unstegano(IMAGE), X, Y, 'd')))
        elif chiffre == '3':
            X = input("Choisir une lettre du clavier: ")
            print((cf.cesar(st.unstegano(IMAGE), X, 'd')))
        else:
            print(st.unstegano(IMAGE))
    else:
        print("Help: pour utiliser se programme utiliser les choix: 1 ou 2")
    print(END)


def stego_pict():
    fc.menu_stego()
    choix = input("Entrer votre choix: ")
    if choix == '1':
        IM1 = input("Nom de l'image vecteur à utiliser: ")
        IM2 = input("Nom de l'image à camoufler: ")
        st.stegpict(IM1, IM2, CODE)
        print("La nouvelle image est générée: ", CODE)
        print(END)
    else:
        IM = input("Nom de l'image: ")
        st.unstegpict(IM, RECOVERY)
        print("L'image est récupérée: ", RECOVERY)
        print(END)
