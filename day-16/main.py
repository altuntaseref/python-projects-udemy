# from turtle import Turtle, Screen
#
# breaks = Turtle()
# breaks.shape("turtle")
# breaks.color("blue")
# breaks.forward(100)
# my_screen= Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

my_ascii = PrettyTable()
my_ascii.add_column("Pokemon",["Pikachu","Scurtle"])
my_ascii.add_column("Type",["Electric","Water"])
my_ascii.align = "r"
print(my_ascii)
