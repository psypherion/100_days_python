# importing necessary libraries

from turtle import Screen
from paddle import Pad
from ball import Ball
import time
from scoreboard import ScoreBoard

# Screen

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.screensize(canvwidth=800, canvheight=600)
screen.tracer(0)

# Creating Paddle
r_pad = Pad((380, 0))
l_pad = Pad((-380, 0))

# Creating the Ball

ball = Ball()

# Showing Score :

scoreboard = ScoreBoard()

# Listening user input to move the paddles :

screen.listen()
screen.onkeypress(r_pad.up, "Up")
screen.onkeypress(r_pad.down, "Down")
screen.onkeypress(l_pad.up, "w")
screen.onkeypress(l_pad.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)   # taking some times before initiating the loop for next time
    screen.update()   # updating the screen as screen tracer s initialised to false
    ball.move()       # moving the ball
    # detecting Collision with Wall
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    # detection with paddle
    if ball.distance(r_pad) < 28 and ball.xcor() > 320 or ball.distance(l_pad) < 28 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when right pad misses
    if ball.xcor() > 400:
        ball.ball_reset()
        scoreboard.l_point()

    # detect when left paddle misses
    if ball.xcor() < -400:
        ball.ball_reset()
        scoreboard.r_point()

screen.exitonclick()
