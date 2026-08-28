import turtle
import random

turtle.colormode(255)
t = turtle.Turtle()
t.speed("fastest")
t.penup()
color_list = [(145, 91, 40), (110, 166, 213), (55, 108, 143), (204, 223, 240), (208, 151, 81), (20, 40, 55),(188, 136, 43), (71, 38, 19), (98, 73, 16), (127, 37, 20), (76, 96, 81), (65, 20, 26), (30, 42,35), (154, 195, 233), (73, 135, 187), (234, 200, 104), (195, 102, 71), (28, 76, 91), (115, 80, 86), (112, 32, 37), (237, 218, 196), (48, 62, 83), (67, 143, 183), (171, 148, 155), (46, 76, 59), (141, 162, 146), (238, 244, 241), (229, 215, 221), (112, 140, 111), (157, 201, 223)]
t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)


    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


s = turtle.Screen()
s.exitonclick()