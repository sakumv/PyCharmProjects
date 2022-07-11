import random
import turtle
from turtle import Turtle,Screen

########hirst diagram#######
#import color from the picture downloaded
# import colorgram
# h_colors = colorgram.extract("hirst.jpg",20)
# fcolor = []
# for color in h_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     fcolor.append(new_color)
# print (fcolor)

color_list = [(197, 165, 119), (144, 81, 56), (220, 201, 138), (61, 95, 121), (165, 150, 54), (136, 162, 180), (131, 34, 23), (52, 119, 87), (73, 37, 29), (190, 96, 82), (145, 177, 150), (100, 76, 80), (165, 147, 157), (21, 92, 68), (28, 59, 75), (225, 177, 167)]

turtle.colormode(255)
#Get the turtle object and screen object
my_turtle = Turtle()
my_turtle.color("teal") #default is teal color
my_screen = Screen()

def get_hcolors(row_color):
    my_turtle.penup()
    my_turtle.setx(-200)
    i = 0
    while i < row_color:
        cot = random.choice(color_list)
        my_turtle.pendown()
        my_turtle.dot(20, cot)
        my_turtle.penup()
        my_turtle.forward(50)
        i += 1

my_turtle.penup()
my_turtle.sety(-250)
for i in range(0,10):
    get_hcolors(10)
    my_turtle.setx(-200)
    y = my_turtle.ycor()
    my_turtle.sety(y+50)

my_turtle.hideturtle()

my_screen.exitonclick()
