import random
import turtle
from turtle import Turtle, Screen
import colorgram

my_turtle = Turtle()

my_turtle.shape("turtle")
my_turtle.color("green")

colors = ["green", "brown", "teal", "blue", "dark red","khaki", "slate blue", "purple", "seashell"]
direction = ["0","90","180","270"]
turtle.colormode(255)

# for _ in range(4):
#     my_turtle.forward(100)
#     my_turtle.right(90)
#
# for _ in range(50) :
#     my_turtle.forward(10)
#     tx = my_turtle.xcor()
#     ty = my_turtle.ycor()
#     my_turtle.goto(tx+10, ty)

#for random color
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    my_tuple = (r,g,b)
    return my_tuple


#for creating dotted line
def draw_dottedline(space, x):
    for i in range(x):
        my_turtle.pendown()
        my_turtle.forward(space)
        my_turtle.penup()
        my_turtle.forward(space)


# Main Section
# my_turtle.penup()
# draw_dottedline(10, 8)

# hide the turtle
#my_turtle.hideturtle()

#for creating different shape of polygon
def draw_shape(distance,sides):
    angle = 360 / int(sides)
    #theColor = random.choice(colors)
    #get the color from random colors
    thecolor = random_color()
    my_turtle.color(thecolor)
    for _ in range(sides):
        my_turtle.forward(distance)
        my_turtle.left(angle)


# for i in range(3,10):
#     draw_shape(100,i)


def draw_random_walker():
    my_turtle.color(random_color())
    angle_choice = random.choice(direction)
    my_turtle.setheading(int(random.choice(direction)))
    my_turtle.forward(20)


# my_turtle.pensize(10)
# my_turtle.speed(9)
# for i in range(1,200):
#     draw_random_walker()


def draw_spiralcircle(size_gap):
    for i in range(int(360 / size_gap)):
        current_heading = my_turtle.heading()
        my_turtle.setheading(my_turtle.heading() + size_gap)
        #set the color
        my_turtle.color(random_color())
        my_turtle.circle(100)


# my_turtle.speed(0)
# draw_spiralcircle(5)

########hirst diagram#######
##import color from the picture downloaded
h_colors = colorgram.extract("hirst.jpg",20)

def get_hcolors(h_colors,row_color):
    my_turtle.penup()
    my_turtle.setx(-100)
    for i in range(0,row_color):
        first_color = h_colors[random.randint(0,14)]
        rgb = first_color.rgb
        my_turtle.color(rgb)
        my_turtle.pendown()
        my_turtle.dot(10, rgb)
        my_turtle.penup()
        my_turtle.forward(20)


for i in range(0,15):
    get_hcolors(h_colors,15)
    my_turtle.setx(-100)
    y = my_turtle.ycor()
    my_turtle.sety(y+20)




# for making to stay in the window
my_screen = Screen()
my_screen.exitonclick()
