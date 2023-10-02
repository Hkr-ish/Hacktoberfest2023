from turtle import Turtle
import random
import turtle as t
arrow=Turtle()
t.colormode(255)
arrow.speed(40)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color
n=0
while n!=360:
    arrow.color(random_color())
    arrow.circle(50)
    arrow.left(n)
    n+=10
