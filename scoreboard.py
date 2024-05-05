from turtle import Turtle


class Scoreboard(Turtle):
    """Tracks and Displays the Score for Both Players"""
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def scoreboard(self):
        """Displays the current score on the screen"""
        self.clear()

        # Display left score
        self.goto(-100, 220)  # Adjust offset for better positioning
        self.write(self.l_score, align="center", font=("courier", 50, "normal"))

        # Display right score
        self.goto(100, 220)  # Adjust offset for better positioning
        self.write(self.r_score, align="center", font=("courier", 50, "normal"))

    def update_l(self):
        """Updates the left player's score and displays the scoreboard"""
        self.l_score += 1
        self.scoreboard()

    def update_r(self):
        """Updates the right player's score and displays the scoreboard"""
        self.r_score += 1
        self.scoreboard()
