from turtle import Turtle, Screen
import random 

s = Screen()

colors = ["red", "blue", "green", "yellow", "Orange"]
positions =[150, 120, 90, 60, 30]

turtles = []

for i in range(5):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-350, positions[i])
    turtles.append(t)

race_on = True
while race_on:
    for t in turtles:
        t.forward(random.randint(10,20))
        if t.xcor() > 350:
            race_on = False
            print(f"{t.pencolor()} turtle wins!")
            break

s.exitonclick()