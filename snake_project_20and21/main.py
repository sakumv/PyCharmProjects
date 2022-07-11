from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.setup(width=600,height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_score = Scoreboard()

is_game_on = True

#turn the graphics off so that it doesnt show as 3 segments
my_screen.tracer(0)

#create a snake object
my_snake = Snake()
my_food = Food()


my_screen.listen()
my_screen.onkey(my_snake.up, "Up")
my_screen.onkey(my_snake.down, "Down")
my_screen.onkey(my_snake.left, "Left")
my_screen.onkey(my_snake.right, "Right")

while is_game_on:
    #get the snake seements to move forward
    my_screen.update()
    time.sleep(0.1)
    my_snake.move()

    #Detect the collision of food
    if my_snake.head.distance(my_food) < 15:
        my_food.refresh()
        my_score.increase_score()
        my_snake.extend_snake()

    #Detect the collision of Wall
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280 :
        #is_game_on = False
        my_score.reset_score()
        my_snake.reset_snake()

    #Detect collision with tail
    for seg in my_snake.my_snake[1:]:
        #if the segment is head, then pass
        # if seg == my_snake.head:
        #     pass
        if my_snake.head.distance(seg) < 10 :
            #is_game_on = False
            my_score.reset_score()
            my_snake.reset_snake()

my_screen.exitonclick()


# Slicng
# piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
# piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")
#
# print(piano_tuple[1:])

#######Sample class for inheritance
# class Animal:
#
#     def __init__(self):
#         self.num_eyes = 2
#
#     def breathe(self):
#         print("I can breathe..Inhale .. Exhale")
#
# class Fish(Animal):
#
#     def __init__(self):
#         super().__init__()
#
#     def swim(self):
#         print("I can swim too")
#
#     def breathe(self):
#         super().breathe()
#         print("I can breath underwater only")
#
#
# nemo = Fish()
# nemo.breathe()
# nemo.swim()