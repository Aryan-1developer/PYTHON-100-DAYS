from turtle import  Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.shape("circle")
        self.color("Blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()
        self.showturtle()

    def refresh(self):
        position = (random.randint(-280, 280), random.randint(-280, 280))
        self.goto(position)

