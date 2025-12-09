# scoreboard.py
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear and redraw the score display."""
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)

    def left_point(self):
        """Add a point to the left player."""
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        """Add a point to the right player."""
        self.right_score += 1
        self.update_scoreboard()
