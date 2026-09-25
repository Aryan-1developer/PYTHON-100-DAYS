import random
from turtle import Screen, Turtle
import time
import snake 
from food import Food
from scoreBoard import Scoreboard


s = Screen()
s.setup(width=600, height=600)
s.title("Snake Game")
s.bgcolor("black")
s.tracer(0)

snake = snake.Snake()
food = Food()
scoreboard = Scoreboard()


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
    
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    
s.exitonclick()