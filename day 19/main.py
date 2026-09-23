from turtle import Turtle, Screen 
t = Turtle()
def move_forwards():
    t.forward(10)

def turn_right():
    t.right(10)

def turn_left():
    t.left(10)

def move_backward():
    t.backward(10)

def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

s = Screen()
s.listen()
s.onkey(key ="w", fun = move_forwards)
s.onkey(key = "s", fun = move_backward)
s.onkey(key = "a", fun = turn_left)
s.onkey(key = "d", fun = turn_right)
s.onkey(key = "c", fun = clear_screen)

s.exitonclick()

