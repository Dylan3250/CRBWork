from random import randint

# Fonction qui permet de lancer 2 dés a nombre de fois
# a => INT
def lance(a):
    tableau = []

    # Nombre de lancé à faire
    for i in range(a):
        result = 0

        # Nombre de dé à lancer
        for d in range(2):
            aleatoire = randint(1,6)
            result = result + aleatoire

        # Tableau avec toutes les sommes des dés lancés
        tableau.append(result)

    # Vérification des résultats (de 1 à 12)
    for x in range(1, 13):
        compteur = 0

        # Boucle qui parcourt le tableau pour compter le nombre de fois qu'il y a eu X nombre
        for i in range(len(tableau)):
            if tableau[i] == x:
                compteur = compteur + 1

        print("L'addition des deux dés est arrivée " + (str(compteur)) + " fois à " + str(x) + " !")

# Appel à la fonction
lance(1000)