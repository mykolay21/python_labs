# main.py
import time
from time import sleep
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard



SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BORDER_MARGIN = 20  # margin from window edge for the border


def create_screen() -> Screen:
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.title("Arcade Game — Pong")
    screen.bgcolor("black")
    # turn off automatic drawing updates for smoother control during setup
    screen.tracer(0)
    return screen


def draw_border(screen: Screen, margin: int = BORDER_MARGIN):
    """Draw a simple white rectangular border around the play area."""
    border = Turtle()
    border.hideturtle()
    border.penup()
    border.pensize(3)
    border.color("white")
    left = -SCREEN_WIDTH // 2 + margin
    top = SCREEN_HEIGHT // 2 - margin

    border.goto(left, top)
    border.pendown()
    for _ in range(4):
        # draw rectangle: width then height alternately
        if _ % 2 == 0:
            border.forward(SCREEN_WIDTH - 2 * margin)
        else:
            border.forward(SCREEN_HEIGHT - 2 * margin)
        border.right(90)
    border.penup()


def main():
    screen = create_screen()
    # Optional: draw a border so it looks like a game board.
    draw_border(screen)


    # Create paddles
    right_paddle = Paddle(x_pos=350, y_pos=0)
    left_paddle = Paddle(x_pos=-350, y_pos=0)
    ball = Ball()
    scoreboard = Scoreboard()
    # Keyboard bindings
    screen.listen()
    screen.onkeypress(right_paddle.move_up, "Up")
    screen.onkeypress(right_paddle.move_down, "Down")

    screen.onkeypress(left_paddle.move_up, "w")
    screen.onkeypress(left_paddle.move_down, "s")

    game_is_on = True
    # Game loop
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()

        sleep(0.01)
        ball.move()

        # Bounce off top/bottom walls
        if ball.ycor() > (SCREEN_HEIGHT // 2 - 20) or ball.ycor() < -(SCREEN_HEIGHT // 2 - 20):
            ball.bounce_y()

        # Bounce off paddles
        if (ball.xcor() > 320 and ball.distance(right_paddle) < 50) or \
                (ball.xcor() < -320 and ball.distance(left_paddle) < 50):
            ball.bounce_x()

        # Detect out of bounds (score situation)
        if ball.xcor() > SCREEN_WIDTH // 2 - 10:
            ball.reset_position()
            scoreboard.left_point()

        if ball.xcor() < -(SCREEN_WIDTH // 2 - 10):
            ball.reset_position()
            scoreboard.right_point()

if __name__ == "__main__":
    main()
