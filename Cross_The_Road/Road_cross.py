import turtle
import random 
from turtle import Turtle ,Screen
import Turtle_to_crossTHEROAD

s = Screen()
s.setup(width=800, height=600 , startx=0, starty=0)
s.bgcolor("black")
s.title("Cross The Road")
s.tracer(0)

red_turtle = Turtle_to_crossTHEROAD.Turtle()


s.listen()
s.onkey(red_turtle.move, "Up")
s.onkey(red_turtle.move, "Down")
s.exitonclick()
