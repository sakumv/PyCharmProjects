from turtle import Turtle,Screen
import turtle
import random

my_screen = Screen()

t_colors = ["red", "blue", "purple", "pink", "yellow", "orange", "green"]

#turtle race project
my_screen.setup(width=500, height = 400)
my_choice = turtle.textinput(title = "Make a choice",prompt="Which color turtle you want to win? ")

my_turtle = []
ycor = -90
print(len(t_colors))

for i in range(0, len(t_colors)):
    new_turtle = Turtle("turtle")
    new_turtle.color(t_colors[i])
    new_turtle.penup()
    my_turtle.append(new_turtle)
    my_turtle[i].goto(x=-230, y=ycor)
    ycor += 30

is_race_on = False

if my_choice:
    is_race_on = True


while is_race_on:
    for turtles in my_turtle:
        if turtles.xcor() >= 230 :
            is_race_on = False
            if turtles.pencolor() == my_choice:
                print(f"You won ! The winning color is {turtles.pencolor()}")
            else:
                print(f"You lost. The winning color is {turtles.pencolor()}")
        random_dis = random.randint(0,10)
        turtles.forward(random_dis)






my_screen.exitonclick()



##Commented as it is a practice
#
#
# def moveforward():
#     my_turtle.forward(10)
#
#
# def movebackward():
#     my_turtle.backward(10)
#
#
# def moveclock():
#     my_turtle.left(10)
#
#
# def moveanticlock():
#     my_turtle.right(10)
#
# def clearscreen():
#     my_turtle.home()
#     my_turtle.clear()
#
#
# #WSADC
#
# my_screen.listen()
# my_screen.onkey(key= "c",fun=clearscreen)
# my_screen.onkey(key= "w",fun=moveforward)
# my_screen.onkey(key="s",fun=movebackward)
# my_screen.onkey(key="a",fun=moveclock)
# my_screen.onkey(key="d",fun=moveanticlock)
#






