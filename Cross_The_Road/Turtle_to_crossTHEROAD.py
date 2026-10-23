from turtle import Turtle ,Screen

class Turtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Red")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_y = self.ycor() + self.y_move
        self.goto(0, new_y)

