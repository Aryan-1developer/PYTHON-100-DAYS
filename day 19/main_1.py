from turtle import Turtle , Screen 

t = Turtle()
def make_circle():
    t.left(90)
    t.penup()
    t.forward(100)
    t.pendown()
    t.right(90)
    t.circle(50)
    t.penup()
    t.home()

def Vertical_line():
    t.pendown()
    t.left(90)
    t.forward(100)
    t.left(180)
    t.forward(200)

def inverted_v_leg():
    t.left(60)
    t.forward(65)
    t.backward(65)
    t.right(120)
    t.forward(65)
    t.penup()
    t.home()

def inverted_v_arm():
    t.left(90)
    t.forward(35)
    t.pendown()
    t.left(180)
    inverted_v_leg()



make_circle()
Vertical_line()
inverted_v_leg()
inverted_v_arm()

s = Screen()
s.exitonclick()
