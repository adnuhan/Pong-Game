import scoreboard
import paddle
import turtle
import ball
import time


class SinglePlayer:
    """Lets you practice against AI"""
    def __init__(self):
        self.window = turtle.Screen()
        self.window.setup(width=800, height=600)
        self.window.title("Pong Game")
        self.window.bgcolor("Black")
        self.window.tracer(0)

        player_paddle = paddle.Paddle((370, 5))
        computer_paddle = paddle.Paddle((-380, 5))
        score = scoreboard.Scoreboard()
        self.ball = ball.Ball()

        self.window.listen()
        self.window.onkey(player_paddle.go_up, "Up")
        self.window.onkey(player_paddle.go_down, "Down")

        while True:
            time.sleep(self.ball.ball_speed)
            self.window.update()
            self.ball.move()
            score.scoreboard()

            # blah blah blah
            if self.ball.xcor() < 0:
                computer_paddle.move(self.ball.ycor())

            # Detect Collision with Top and Bottom Wall
            if self.ball.ycor() > 275 or self.ball.ycor() < -275:
                self.ball.bounce_y()

            # Detect Collision with Paddle
            if (self.ball.distance(player_paddle) < 40 and self.ball.xcor() > 320 or self.ball.distance(computer_paddle)
                    < 40 and self.ball.xcor() < -320):
                self.ball.bounce_x()

            # Detect Player Paddle Misses
            if self.ball.xcor() > 380:
                self.ball.rest_position()
                score.update_r()

            # Detect Computer Paddle Misses
            if self.ball.xcor() < -380:
                self.ball.rest_position()
                score.update_l()
