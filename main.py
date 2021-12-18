from turtle import Screen
from ball import Ball
from bat import Bat
from score import Score
from wall import Wall

HEIGHT = 600
WIDTH = 800

BALL_MAX_XCOR = int(round(WIDTH / 2)) - 20
BALL_MAX_YCOR = int(round(HEIGHT / 2)) - 20
BALL_ANGLE_INCREASE = 90

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Bounce Game")
screen.bgcolor("black")
screen.tracer(0)

bat = Bat("down")

screen.listen()
screen.onkey(bat.move_right, "Right")
screen.onkey(bat.move_left, "Left")

# TODO: make the bats move while the key is pressed

ball = Ball()
current_ball_angle = 45
ball.setheading(current_ball_angle)
hit = False


wall = Wall()

game_on = True
while game_on:

    if ball.distance(bat) < 65 and ball.ycor() < -(BALL_MAX_YCOR - 20) \
            or ball.xcor() < -BALL_MAX_XCOR \
            or ball.xcor() > BALL_MAX_XCOR \
            or ball.ycor() > BALL_MAX_YCOR:
        hit = True

    elif ball.ycor() < -BALL_MAX_YCOR:
        game_on = False
        Score()

    hit = wall.wall_break(ball, hit)
    if hit:
        current_ball_angle += BALL_ANGLE_INCREASE
        ball.setheading(current_ball_angle)
        hit = False
    ball.move()
    screen.update()

screen.exitonclick()
