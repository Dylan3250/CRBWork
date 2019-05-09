info = input("Veuillez rentrer une note (stop)")
tableau = [float(info)]

while info != 'stop':
    print('--> ' + str(info) + '\tSomme actuelle : ' + str(sum(tableau)), end="\n")
    info = input("Veuillez rentrer une note (stop)")
    if info != 'stop':
        tableau.append(float(info))

moyenne = sum(tableau)/len(tableau)
print('Nombre de notes : ' + str(len(tableau)) + '\nLa moyenne est de ' + str(moyenne))