from turtle import *

def axe(max):
    up()
    goto(max, 0)
    down()
    goto(-max, 0)

    up()
    goto(0, max)
    down()
    goto(0, -max)

def point(max, bond=50):
    axe(max+20)

    depart = bond
    fin = -max

    while fin < 0:
        up()
        goto(fin, 0)
        down()
        goto(0, depart)
        depart += bond
        fin += bond



point(200, 10)
mainloop()