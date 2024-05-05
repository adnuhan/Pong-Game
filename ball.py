from turtle import Turtle


class Ball(Turtle):
    """Defines a Ball that Moves and Responds to Collisions with Walls and Paddles"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("White")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        """Moves the ball by updating its x and y coordinates"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Handles the Ball Bouncing off Top/Bottom Wall"""
        self.y_move *= -1

    def bounce_x(self):
        """Handles the Ball Bouncing off the Left/Right sides with Gradual Speed Increase"""
        self.x_move *= -1
        self.ball_speed *= 0.9

    def rest_position(self):
        """Rests the Ball Position and Speed"""
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()
