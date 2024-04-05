
# import turtle

# from turtle import Turtle, Screen
# timmy = Turtle()
 
 
# print(timmy)

# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# my_screen = Screen()


# print(my_screen)

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

print(table)

table.add_column("pokemon",["Pickachu","Squirtle","charmander"])
table.add_column("type",["Electric","Water","Fire"])

table.align  = "l"

print(table)