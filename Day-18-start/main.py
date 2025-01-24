from turtle import Turtle, Screen
import random

timmy = Turtle()

timmy.shape("turtle")
timmy.color("red", "green")


# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

colours = ['black','purple','red','green']
def draw_shape(num_sides):
    angel = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angel)


for shape_side_n in range(3, 11):
    timmy.color(random.choice(colours))
    draw_shape(shape_side_n)





screen = Screen()
screen.exitonclick()
