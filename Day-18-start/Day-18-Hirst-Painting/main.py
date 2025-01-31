# import colorgram
import turtle as turtle_module
import random

from PIL.ImageChops import screen

# fruits = ["apple", "banana", "cherry"]
#
# for index, fruit in enumerate(fruits):
#     print(f"Index: {index}, Fruit: {fruit}")


# Extract 6 colors from an image.
# colors = colorgram.extract('hirst_image.jpg', 6)
#
# print("Extracted colors:")
#
# rgb_colors = []

# Loop through the extracted colors and display details
# for i, color in enumerate(colors):
#     rgb = color.rgb  # RGB color tuple
#     hsl = color.hsl  # HSL color tuple
#     proportion = color.proportion  # Proportion of the color in the image
#
#     print(f"Color {i+1}:")
#     print(f"  RGB: {rgb}")
#     print(f"  HSL: {hsl}")
#     print(f"  Proportion: {proportion:.2%}\n")
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(254, 247, 252), (240, 252, 246), (246, 249, 253), (242, 233, 55), (184, 14, 29)]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
       tim.setheading(90)
       tim.forward(50)
       tim.setheading(180)
       tim.forward(500)
       tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
