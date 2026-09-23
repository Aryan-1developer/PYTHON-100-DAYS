from turtle import Screen, Turtle
import time
import snake 
import random 



s = Screen()
s.setup(width=600, height=600)
s.title("Snake Game")
s.bgcolor("black")
s.tracer(0)

snake = snake.Snake()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    s.update() 
    time.sleep(0.1)     
    snake.move()
    
    
        





s.exitonclick()