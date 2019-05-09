nb = int(input('Ecrire un nombre :'))
if nb > 0:
    print(str(nb) + " est un nombre positif")
elif nb<0:
    print(str(nb) + " est un nombre négatif")
else:
    print(str(nb) + " est zéro")