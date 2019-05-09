from random import *

nombre = randint(1, 100)
compte = 0
resultat = int(input('Essayez de trouver le nombre compris entre 1 et 100 :'))

while resultat != nombre:
    if nombre > resultat:
        print(str(resultat) + ' est trop petit')
    else:
        print(str(resultat) + ' est plus grand')

    resultat = int(input('Essayez de trouver le nombre compris entre 1 et 100 :'))

    compte = compte + 1

print("Bravo, le nombre est bien " + str(nombre) + " ! Tu l'as trouvé en " + str(compte) + " coups !")