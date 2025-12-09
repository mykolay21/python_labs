# ball.py
from turtle import Turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("normal")
        # Initial movement increments
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1

    def move(self):
        """Move ball by its current increments."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Reverse vertical direction (when hitting top/bottom)."""
        self.y_move *= -1

    def bounce_x(self):
        """Reverse horizontal direction (when hitting a paddle)."""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Send ball back to center and reverse direction (point scored)."""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
