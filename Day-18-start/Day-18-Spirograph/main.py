import turtle as t
import random, time, math

from click import pause

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########
def  draw_spirograph(size_of_gap):
   tim.speed("fastest")
   for _ in range(int(360/size_of_gap)):
       tim.color(random_color())
       tim.circle(100)
       tim.setheading(tim.heading()+10)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()