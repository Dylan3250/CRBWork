from math import *
racine = []

a = int(input("Quel est le coefficient a ?"))
b = int(input("Quel est le coefficient b ?"))
c = int(input("Quel est le coefficient c ?"))

x = 1  # debug

discriminant = b**2 - 4*a*c

if discriminant > 0 :
    # Strictement positif => 2 solutions
    racine.append((-b + sqrt(discriminant))/2*a)
    racine.append((-b - sqrt(discriminant))/2*a)
elif discriminant == 0:
    # Strictement est nulle => 1 solution
    racine.append(-b/2*a)


print('Valeur du discriminant : ' + str(discriminant))
print('Nombre de racine : ' + str(len(racine)))
print('Valeur de(s) la/les racine(s) : ' + str(racine))