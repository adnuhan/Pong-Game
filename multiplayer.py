import scoreboard
import paddle
import turtle
import ball
import time


class Multiplayer:
    """Lets you challenge your friends"""
    def __init__(self):
        self.window = turtle.Screen()
        self.window.setup(width=800, height=600)
        self.window.title("Pong Game")
        self.window.bgcolor("Black")
        self.window.tracer(0)

        right_paddle = paddle.Paddle((370, 5))
        left_paddle = paddle.Paddle((-380, 5))
        score = scoreboard.Scoreboard()
        self.ball = ball.Ball()

        self.window.listen()
        self.window.onkey(right_paddle.go_up, "Up")
        self.window.onkey(right_paddle.go_down, "Down")
        self.window.onkey(left_paddle.go_up, "w")
        self.window.onkey(left_paddle.go_down, "s")

        while True:
            time.sleep(self.ball.ball_speed)
            self.window.update()
            self.ball.move()
            score.scoreboard()

            # Detect Collision with Top and Bottom Wall
            if self.ball.ycor() > 275 or self.ball.ycor() < -275:
                self.ball.bounce_y()

            # Detect Collision with Paddle
            if (self.ball.distance(right_paddle) < 50 and self.ball.xcor() > 320 or self.ball.distance(left_paddle) < 50
                    and self.ball.xcor() < -320):
                self.ball.bounce_x()

            # Detect Right Paddle Misses
            if self.ball.xcor() > 380:
                self.ball.rest_position()
                score.update_r()

            # Detect left Paddle Misses
            if self.ball.xcor() < -380:
                self.ball.rest_position()
                score.update_l()
