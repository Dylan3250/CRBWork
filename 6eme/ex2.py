List = [0] * 10 # Défini un tableau a 10 entrés vide

def setList(List): # Fonction qui demande a l'utilisateur les nombres pour remplir le tableau
    for i in range(len(List)): # Boucle sur la longeur de base du tableau
        List[i] = int(input("Veuillez indiquer le nombre n°" + str(i+1))) # Modifie le tableau en y ajoutant les nombres donnés

def getList(List): # Fonction qui permet d'ordonner et afficher le tableau
    setList(List) # Appel de la fonction pour remplir le tableau avec les données de l'utilisateur
    List.sort() # Ordonne le tableau avec une fonction de base
    for i in range(len(List)): # Boucle sur la grandeur du tableau défini de base
        List[i] = List[i]*2 # Multiplie tous les éléments du tableau

getList(List) # Calcul et défini le tableau en fonction des valeurs entrées par l'utilisateur
print(List) # Affiche le tableau final