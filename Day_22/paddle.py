# paddle.py
from turtle import Turtle

SCREEN_HEIGHT = 600


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        # stretch square shape: width = 20, height = 100
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_pos, y_pos)

    def move_up(self):
        new_y = self.ycor() + 20
        if new_y < (SCREEN_HEIGHT // 2 - 50):  # keep inside window
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        if new_y > -(SCREEN_HEIGHT // 2 - 50):
            self.goto(self.xcor(), new_y)
