import turtle as t
import random 
from turtle import Screen

tim = t.Turtle()
tim.speed("fastest")
tim.pensize(10)
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return(r, g, b)


directions = [90, 180, 270, 0]


for _ in range(200):
    tim.forward(random.randint(50,100))
    tim.setheading(random.choice(directions))
    tim.pencolor(random_color())

s = Screen()
s.exitonclick()