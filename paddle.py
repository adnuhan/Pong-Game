from turtle import Turtle
import ball


class Paddle(Turtle):
    """Creates a Paddle for the Player to hit the ball with"""
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """Moves the Paddle Upward"""
        new_y = self.ycor() + 30
        if new_y < 250:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        """Moves the Paddle Downward"""
        new_y = self.ycor() - 30
        if new_y > -250:
            self.goto(self.xcor(), new_y)

    def move(self, y):
        """Moves the Paddle Upward or Downward"""
        if -250 < y < 250:
            self.sety(y)
