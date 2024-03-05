# import another_module
# print(another_module.another_variable)
import turtle
from turtle import Turtle, Screen
#
# timmy = Turtle()
#
# print(timmy)
# timmy.shape("turtle")
# my_screen = Screen()
# turtle.color("coral")
# turtle.forward(100)
# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pockemon Nname", ["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
table.add_column("Type", ["Electric", "Water", "Fire","","","",""])
table.header_style = "upper"
table.align = 'l'


print(table)


print("|Pockemon Nname | Type |")
print("_____________________________")
