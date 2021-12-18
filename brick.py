from turtle import Turtle

bricks = []


class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.shape("square")
        self.color("red")
        self.setheading(0)

    @classmethod
    def _multiple(cls, count):
        for i in range(count):
            obj = cls()
            bricks.append(obj)
        return bricks
