# -*- coding: utf-8 -*-
"""
@authors: Cyril Génisson
@file: stegano.py

@project: Colibri
@licence: GPLv3
"""
from PIL import Image
from base64 import b64decode, b64encode
import fonctions as fc


def stegano(file, message, save):
    ''' Encode le message dans l'image file.'''
    image = Image.open(file)
    nc, nl = image.size
    if len(image.split()) == 4:
        red, green, blue, alpha = image.split()
    else:
        red, green, blue = image.split()
    array = list(red.getdata())
    binaire = fc.text2bin(message)
    for k in range(len(binaire)):
        if binaire[k] == '1':
            if fc.parite(array[k]):
                array[k] += 1  # Valeur à mettre à 255 pour voir les modifs
        else:
            if fc.parite(array[k]) is False:
                array[k] -= 1  # Valeur à mettre à 255 pour voir les modifs
    for k in range(len(binaire), len(binaire) + 16):
        if fc.parite(array[k]):
            array[k] += 1
    red2 = Image.new('L', (nc, nl))
    red2.putdata(array)
    resultat = Image.merge("RGB", (red2, green, blue))
    resultat.save(save)


def unstegano(file):
    ''' Récupère le message caché dans l'image file. '''
    image = Image.open(file)
    red, green, blue = image.split()
    array = list(red.getdata())
    message = ''
    for k in range(len(array)):
        if fc.parite(array[k]):
            message += '0'
        else:
            message += '1'
        if message[len(message)-16:] == '1111111111111111':
            break
    return fc.bin2text(message[:-16])


def stegpict(im1, im2, save):
    ''' Camoufle im2 dans im1 et sauvegarde le résultat dans save. '''
    secret = open(im2, "rb")  # Ouverture en binaire et lecture seul de im2
    payload = secret.read()  # Chargement du fichier dans payload (buffer)
    secret.close()
    payload = b64encode(payload)

    # Conversion de la liste payload en une chaîne de caractères ASCII
    message = ""
    for k in range(len(payload)):
        message += chr(payload[k])
    stegano(im1, message, save)


def unstegpict(file, save):
    ''' Récupère l'image camouflée dans file et la sauvegarde dans save. '''
    secret = open(save, "wb")
    message = unstegano(file)
    secret.write(b64decode(message + '='))
    secret.close()
