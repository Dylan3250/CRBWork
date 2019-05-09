a = 5
b = 10
nb = int(input('Ecrire un nombre équivaut à 5 ou 10 ou 3 :'))
if a == nb:
    a = a+5
    print('a vaut : ' + str(a))
elif b == nb:
    b = b + 20
    print('Le nombre vaut ' + str(b))
else:
    print('Le nombre vaut ' + str(nb))