nombre = int(input('Veuillez indiquer un nombre'))
tableau = []
nombre_base = nombre

for i in range(2, int(nombre)):
    if nombre%i == 0:
        tableau.append(str(i))
        nombre = nombre / i

        while nombre%i == 0:
            nombre = nombre / i
            tableau.append(str(i))

if not tableau:
    print(str(nombre_base) + ' est un nombre premier.')
else:
    print(str(nombre_base) + ' n\'est pas un nombre premier.\t' + str(nombre_base) + " = " + ' * '.join(tableau))