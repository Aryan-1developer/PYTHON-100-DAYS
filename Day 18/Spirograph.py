import turtle as t
import random 
from turtle import Screen

t.speed("fastest")

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return(r, g, b)

for _ in range(60):
    t.circle(175)
    t.left(6)
    t.pencolor(random_color())


s = Screen()
s.exitonclick()