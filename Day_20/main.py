from turtle import Screen
import random
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

scoreboard = Scoreboard()

screen = Screen()
screen.setup(width = 600 , height= 600)
screen.bgcolor("black")
screen.title("My snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")

snake_speed = 0.3   # start slower
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(snake_speed)

    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        scoreboard.increase_score()
        food.refresh()

    # Detect collision with wall
    if (
         snake.head.xcor() > 280
         or snake.head.xcor() < -280
         or snake.head.ycor() > 280
         or snake.head.ycor() < -280
        ):
            game_is_on = False
            scoreboard.game_over()

    #Detect collision with tail.
    for segment in snake.segments[1:]:
        if  snake.head.distance(segment) < 10:
           game_is_on = False
           scoreboard.game_over()


screen.exitonclick()

screen.exitonclick()