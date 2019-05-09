from random import random

for i in range(100):
    pourcentage = random()

    if pourcentage <= 0.1:
        result = 1
    elif pourcentage <= 0.25:
        result = 2
    elif pourcentage <= 0.4:
        result = 3
    elif pourcentage <= 0.55:
        result = 4
    elif pourcentage <= 0.7:
        result = 5
    elif pourcentage > 0.7:
        result = 6

    print('Le dé lancé donne comme résultat ' + str(result))