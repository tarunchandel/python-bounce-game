from brick import Brick

HEIGHT = 600
WIDTH = 800
BAT_SPEED = 80

BRICKS = 55
BRICKS_COLUMNS = 11
BRICKS_ROWS = BRICKS // BRICKS_COLUMNS
bricks_coordinates = []


class Wall:
    def __init__(self):
        self.bricks = Brick._multiple(BRICKS)
        self.setup_wall()

    def setup_wall(self):
        xcor = -360
        ycor = 280
        for i in range(BRICKS_ROWS):
            ycor -= 40
            for j in range(BRICKS_COLUMNS):
                bricks_coordinates.append((xcor + (j * 70), ycor))
        for i in range(len(self.bricks)):
            self.bricks[i].goto(bricks_coordinates[i])

    def wall_break(self, ball, hit):
        for brick in self.bricks:
            if ball.distance(brick) < 20:
                brick.hideturtle()
                self.bricks.remove(brick)
                return True
        return hit
