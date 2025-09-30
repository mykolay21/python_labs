# main.py
from turtle import Screen, Turtle
from paddle import Paddle

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

    # Keyboard bindings
    screen.listen()
    screen.onkeypress(right_paddle.move_up, "Up")
    screen.onkeypress(right_paddle.move_down, "Down")

    screen.onkeypress(left_paddle.move_up, "w")
    screen.onkeypress(left_paddle.move_down, "s")

    # Game loop
    while True:
        screen.update()



if __name__ == "__main__":
    main()
