from turtle import Turtle


class Ball(Turtle):
    """Defines a Ball that Moves and Responds to Collisions with Walls and Paddles"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_axis = 10
        self.y_axis = 10
        self.ball_speed = 0.1

    def move(self):
        """Moves the ball by updating its x and y coordinates"""
        x = self.xcor() + self.x_axis
        y = self.ycor() + self.y_axis
        self.goto(x, y)

    def bounce_y(self):
        """Handles the Ball Bouncing off Top/Bottom Wall with Gradual Speed Increase"""
        self.y_axis *= -1
        self.ball_speed *= 1.1

    def bounce_x(self):
        """Handles the Ball Bouncing off the Left/Right sides with Gradual Speed Increase"""
        self.x_axis *= -1
        self.ball_speed *= 1.1

    def rest_position(self):
        """Rests the Ball Position and Speed"""
        self.goto(0, 0)
        self.bounce_x()
        self.ball_speed = 0.1
