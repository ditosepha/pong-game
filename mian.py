from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.colormode(255)
screen.bgcolor(32, 32, 54)
screen.title("My Pong Game")
screen.tracer(0)


left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    #detect collision with paddle
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50 or ball.xcor() > -320 and ball.distance(left_paddle) < 50:
        print("MADE CONTACT")
        ball.paddle_bounce()


    #detect right paddle miss
    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_point()
    
    #detect left paddle miss
    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()

screen.exitonclick()