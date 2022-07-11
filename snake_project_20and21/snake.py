from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.my_snake = []
        self.createsnake()
        self.head = self.my_snake[0]

    def createsnake(self):
        for i in START_POSITION:
            self.add_snake(i)

    def move(self):
        for seg_pos in range(len(self.my_snake) - 1, 0, -1):
            new_index = seg_pos - 1
            new_x = self.my_snake[new_index].xcor()
            new_y = self.my_snake[new_index].ycor()
            self.my_snake[seg_pos].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_snake(self,position):
        my_s = Turtle("square")
        my_s.color("white")
        my_s.penup()
        my_s.goto(position)
        self.my_snake.append(my_s)

    def reset_snake(self):
        for seg in self.my_snake:
            seg.goto(1000,1000)
        self.my_snake.clear()
        self.createsnake()
        self.head = self.my_snake[0]

    def extend_snake(self):
        self.add_snake(self.my_snake[-1].position())


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
