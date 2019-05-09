nbList = int(input('Combien de nombre avez-vous à élever au carré ?')) # Demande combien de nombre doivent être élevé au carré
List = [0] * nbList # Crée une liste vide de nbList éléments

def auCarre(nb): # Fonction permettant de calculer le carré d'un nombre nb indiqué en paramètre
    return nb**2 # Retourne un nombre au carré

def getList(nbList, List): # Fonction permettant d'ajouter au tableau les carrés
    for i in range(nbList): # Boucle qui tourne le nombre de fois indiqué par nbList
        nbCarre = int(input("Veuillez indiquer le nombre n°" + str(i+1))) # Demande un nombre pour ajouter au tableau
        List[i] = auCarre(nbCarre) # Appel a la fonction auCarre

getList(nbList, List) # Appel la fonction modifiant le tableau en ajoutant en paramètre le nombre d'élément et le tableau pour le modifier par la suite
print(List) # Affiche le tableau modifié