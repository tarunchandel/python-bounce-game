from turtle import Turtle

HEIGHT = 600
WIDTH = 800
SCORE_XCOR = int(round(WIDTH / 2)-30)
SCORE_YCOR = int(round(HEIGHT / 2) - 60)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score: int = 0
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.speed(0)
        self.goto(0, 0)
        self.write(f"G  A  M  E    O  V  E  R  .\nPractice makes you perfect", move=False, align='center', font=('Courier', 20, 'normal'))
