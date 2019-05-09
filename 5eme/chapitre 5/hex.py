from turtle import *
from math import sqrt

speed(10)
def hex():
    for i in range (6):
        forward(30)
        left(60)


def circle(x):
    hex()
    left(30)
    up()
    forward(((sqrt(3)/2)*30)*2)
    down()
    right(30)
    hex()

circle(10)
mainloop()