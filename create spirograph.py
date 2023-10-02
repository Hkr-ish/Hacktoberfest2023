from turtle import Turtle
import random
import turtle as t
rishabh=Turtle()
t.colormode(255)
rishabh.speed(40)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color
n=0
while n!=360:
    rishabh.color(random_color())
    rishabh.circle(50)
    rishabh.left(n)
    n+=10
