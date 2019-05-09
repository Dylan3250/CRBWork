from random import randint
result = 0

# EXERCIE A
for i in range(3):
    aleatoire = randint(1,6)
    result = result + aleatoire
    print("L'un des dés retourne : " + str(aleatoire))

print('La somme totale des dés est de ' + str(result))


# EXERCIE B
for x in range(50):
    result = 0
    for i in range(3):
        aleatoire = randint(1,6)
        result = result + aleatoire
        print("L'un des dés retourne : " + str(aleatoire))
    print('------ Un jet de 3 dés est achevé, leur somme est' + str(result) + ' ! ------')


# EXERCIE C
for x in range(200):
    result = 0
    for i in range(2):
        aleatoire = randint(1,8)
        result = result + aleatoire
        print("L'un des dés retourne : " + str(aleatoire))
    print('------ Un jet de 3 dés est achevé, leur somme est' + str(result) + ' ! ------')