from turtle import *
speed("fastest")

# FONCITON RETOURNE NOMBRE DE NOMBRE PREMIER
def nb_diviseur(nombre):

    count_default = 1
    for i in range(1, int(nombre)):
        if nombre%i == 0:
            count_default = count_default + 1

            if(nombre%i != 0):
                while nombre%i == 0:
                    count_default = count_default + 1

    return count_default



# FONCITON RETOURNE LES CERCLES SUR BASE DE LA TORTUE
def tortue(nb_boucle, nb_premier):
    taille_pas = 8
    color('blue')
    total_tableau = []

    # Boucle créant le tableau des nombres des diviseurs
    for a in range (1, nb_premier+1):
        total_tableau.append(nb_diviseur(a))

    # Boucle affichant la tortue et les cercles
    for i in range (nb_boucle):
        for n in range (2):
            left(90)

            for d in range (i):
                down()
                begin_fill()
                circle(int(round(total_tableau[d]/2)))
                end_fill()
                up()
                forward(taille_pas)

# Nombre de boucle
tortue(1000, 100)

mainloop()