from turtle import Turtle, Screen
import random 

q = Turtle()
w = Turtle()
e = Turtle()
r = Turtle()
t = Turtle()

q.shape("turtle")
q.color("red")
q.penup()
q.goto(-350,160)

w.shape("turtle")
w.color("green")
w.penup()
w.goto(-350,130)

e.shape("turtle")
e.color("blue")
e.penup()
e.goto(-350,100)

r.shape("turtle")
r.color("yellow")
r.penup()
r.goto(-350,70)

t.shape("turtle")
t.color("orange")
t.penup()
t.goto(-350,40)

random.randint(10,20)

on_race = True

while on_race:
    q.forward(random.randint(10,20)) 
    w.forward(random.randint(10,20)) 
    e.forward(random.randint(10,20)) 
    r.forward(random.randint(10,20)) 
    t.forward(random.randint(10,20)) 

if t.xcor() > 350:       # finish line
            race_on = False

            #break

s = Screen()
s.exitonclick()