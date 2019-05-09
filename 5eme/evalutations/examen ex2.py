somme = int(input("Indiquez la somme : "))

# Fonction qui permet de calculer la découpe d'une somme
# Somme => INT
def total(somme):

    tableau = [500, 200, 100, 50, 20, 5, 2, 1]
    total = []

    # Tant que la somme n'est pas égale à zéro
    while somme > 0:

        # Vérifie dans le tableau le nombre de découpage qu'il faut faire
        for i in range(len(tableau)):
            while somme >= tableau[i]:
                somme = somme - tableau[i]
                # Ajoute dans un tableau les billets/pièces requises
                total.append(tableau[i])

    # Compte le nombre de découpage possible
    for d in range(len(tableau)):
        compteur = 0

        # Compte les découpages fait de la somme donnée
        for i in range(len(total)):
            if total[i] == tableau[d]:
                compteur = compteur + 1

        # N'affiche pas de message si ce découage n'existe pas
        if(compteur > 0):
            print("Pour arriver à la somme, il faudra " + (str(compteur)) + " billet(s)/pièce(s) de " + str(tableau[d]) + " euro(s) !")

# Appel à la fonction
total(somme)