from turtle import Screen, Turtle
import random

class Food(Turtle):
    def __init__(self):
        position = (random.randint(-300, 300), random.randint(-300, 300))
        super().__init__(visible=False)
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.speed("fastest")
        self.goto(position)
        self.showturtle()

is_food = True
while is_food:
    raj = Food()
s = Screen()
s.exitonclick()