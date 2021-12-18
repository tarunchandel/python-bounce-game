from turtle import Turtle

HEIGHT = 600
WIDTH = 800
BAT_SPEED = 120
BAT_YCOR = int(round(HEIGHT / 2)) - 20
BAT_MAX_MOVE = int(round(WIDTH / 2)) - BAT_SPEED


class Bat(Turtle):
    def __init__(self, direction):
        super().__init__()
        self.penup()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.shapesize(stretch_len=6, stretch_wid=1)
        self.setheading(0)
        if direction == "down":
            self.goto(0, -BAT_YCOR)

    def move_right(self):
        if self.xcor() < BAT_MAX_MOVE:
            self.forward(BAT_SPEED)

    def move_left(self):
        if self.xcor() > - BAT_MAX_MOVE:
            self.backward(BAT_SPEED)
