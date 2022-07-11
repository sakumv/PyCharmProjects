from turtle import Turtle

SIZE_PADDLE = (20,100)
MOVE_SIZE = 20

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(position)
        self.speed("fastest")


    def up(self):
        y = self.ycor() + MOVE_SIZE
        if self.ycor() < 240:
            self.goto(self.xcor(),y)

    def down(self):
        y = self.ycor() - MOVE_SIZE
        if self.ycor() > -240:
            self.goto(self.xcor(),y)
