total_tableau = []

# FONCITON RETOURNE NOMBRE DE NOMBRE PREMIER
def nb_diviseur(nombre):

    tableau = []

    for i in range(2, int(nombre)):
        if nombre%i == 0:
            tableau.append(str(i))
            nombre = nombre / i

            while nombre%i == 0:
                nombre = nombre / i
                tableau.append(str(i))

    if not tableau:
        return 1
    else:
        return len(tableau)

# Test X nombres
for d in range (300):
    tab = 0

    # Crée un tableau enreigstrant les données (nombre => nombre de diviseur)
    total_tableau.append(nb_diviseur(d))

print(total_tableau)