from turtle import Turtle, Screen
import turtle
import paddle
import time
import ball


s = Screen()
s.setup(width=800, height=600 , startx=0, starty=0)
s.bgcolor("black")
s.title("Ping Pong Game")
s.tracer(0)


paddle_r = paddle.Paddle((380, 0))
paddle_l = paddle.Paddle((-385, 0))
ball = ball.Ball()


s.update()
s.listen()
s.onkey(paddle_r.go_up, "Up")
s.onkey(paddle_r.go_down, "Down")
s.onkey(paddle_l.go_up, "w")
s.onkey(paddle_l.go_down, "s")

l_score = 0
r_score = 0


scoreboard = turtle.Turtle()
scoreboard.color("white") 
scoreboard.penup()
scoreboard.hideturtle()

def update_score():
    scoreboard.clear()
    scoreboard.goto(-100, 200)
    scoreboard.write(l_score, align="center", font=("Courier", 40, "normal"))
    scoreboard.goto(100, 200)
    scoreboard.write(r_score, align="center", font=("Courier", 40, "normal"))

update_score()

while True:
    s.update()
    time.sleep(0.1)
    ball.move()


    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()


    #detect collision with paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 350 :
        ball.paddle_hit()
    
    if ball.distance(paddle_l) < 50 and ball.xcor() < -350:
        ball.paddle_hit()


    if ball.xcor() > 380:
        l_score += 1
        update_score()
        ball.goto(0, 0)
        ball.paddle_hit()

    if ball.xcor() < -380:
        r_score += 1
        update_score()
        ball.goto(0, 0)
        ball.paddle_hit()

s.exitonclick()