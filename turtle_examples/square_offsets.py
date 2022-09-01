from turtle import *
from random import randint

bgcolor("black")
speed(0)

for x in range(1, 400):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    colormode(255)
    pencolor(r, g, b)
    fd(50 + x)
    rt(90.991)
exitonclick()