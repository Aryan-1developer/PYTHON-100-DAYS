import another_module

#print(another_module.another_varable)


from turtle import Turtle , Screen 

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.left(90)
timmy.backward(160)
timmy.left(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(60)
print(timmy)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

