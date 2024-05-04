from turtle import Turtle


class Paddle(Turtle):
    """Creates a Paddle for the Player to hit the ball with"""

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(x, y)

    def up(self):
        """Moves the Paddle Upward"""
        new_y = self.ycor() + 30
        if new_y < 250:
            self.goto(self.xcor(), new_y)

    def down(self):
        """Moves the Paddle Downward"""
        new_y = self.ycor() - 30
        if new_y > -250:
            self.goto(self.xcor(), new_y)

    def move(self, y):
        """Moves the Paddle Upward or Downward"""
        if -250 < y < 250:
            self.sety(y)
