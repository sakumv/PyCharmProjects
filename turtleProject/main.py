# import turtle
#
# #create an object of class Turtle
# my_turtle = turtle.Turtle()
# print(my_turtle)
# my_turtle.shape("turtle")
# my_turtle.color("green")
# my_turtle.home()
# my_turtle.forward(30)
# #create object for screen
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.bgcolor("pink")
# my_screen.exitonclick()
# print(my_turtle.color)


#get the color of turtle changed
import prettytable
#from prettytable import PrettyTable
my_table = prettytable.PrettyTable()

my_table.add_column("Pokemon",["Picachu","Squirtle","Charmander"])
my_table.add_column("Type",["Electric","Water","Fire"])
my_table.align = "l"
print(my_table)