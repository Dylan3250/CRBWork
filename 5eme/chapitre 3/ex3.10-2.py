nb = int(input('Combien voulez-vous tester de nombre ?'))

def is_premier(nombre):

    tableau = []

    for i in range(2, int(nombre)):
        if nombre%i == 0:
            tableau.append(str(i))
            nombre = nombre / i

            while nombre%i == 0:
                nombre = nombre / i
                tableau.append(str(i))

    if not tableau:
        return nombre
    else:
        return tableau

print(is_premier(nb), end='\t')