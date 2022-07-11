from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

r_position = (380,0)
l_position = (-380,0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
###To not to show the animation set the screen tracer to 0
screen.tracer(0)


######to draw a line in the middle
line_turtle = Turtle("square")
line_turtle.color("white")
line_turtle.hideturtle()
line_turtle.penup()

#goto end of the screen and start making a split line
line_turtle.forward(20)
xcor = 0
ycor = -300
line_turtle.left(90)
line_turtle.goto(0, -300)
line_turtle.pensize(3)
line_turtle.speed("fastest")

while ycor < 300:
    ycor += 10
    line_turtle.pendown()
    line_turtle.goto(xcor, ycor)
    ycor += 10
    line_turtle.penup()
    line_turtle.goto(xcor, ycor)

##Create the right paddle
right_paddle = Paddle(r_position)
left_paddle = Paddle(l_position)

#create score board
my_score = Scoreboard()
#Create ball
my_ball = Ball()

### Get the listener for the key
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

is_game_on = True


while is_game_on:
    time.sleep(my_ball.move_speed)
    screen.update()
    my_ball.move()

    #detect collision on the wall
    if my_ball.ycor() > 280 or my_ball.ycor() < -280:
        my_ball.bounce_y()

    #detect collision with right_paddle
    if my_ball.distance(right_paddle) < 50 and my_ball.xcor() > 320:
        my_ball.bounce_x()

    #detect collision with left paddle
    if my_ball.distance(left_paddle) < 50 and my_ball.xcor() > -320:
        my_ball.bounce_x()

    #detect when ball goes out of bounds
    if my_ball.xcor() > 320:
        my_ball.reset_position()
        my_score.l_point()


    #detect when ball goes out of bounds
    if my_ball.xcor() <- 320:
        my_ball.reset_position()
        my_score.r_point()



screen.exitonclick()