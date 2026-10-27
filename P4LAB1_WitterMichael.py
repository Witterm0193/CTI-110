# Michael Witter
# October 27, 2026
# P4LAB1 - Turtle House
# Draw a square house and triangle roof using a while loop and a for loop.

# Pseudocode:
# Import turtle and create the drawing window.
# Set the background to light blue and the turtle to dark blue.
# Move the turtle to the bottom-left corner of the house without drawing.
# Use a while loop to draw four equal sides with 90-degree left turns.
# Move to the top-left corner of the square without drawing.
# Use a for loop to draw three equal sides with 120-degree left turns.
# Hide the turtle and keep the finished drawing window open.

import turtle

window = turtle.Screen()
window.title("P4LAB1 - Michael Witter")
window.setup(700, 650)
window.bgcolor("lightblue")

house_turtle = turtle.Turtle()
house_turtle.shape("turtle")
house_turtle.color("navy")
house_turtle.pensize(4)
house_turtle.speed(4)

# Draw the square walls with a while loop.
house_turtle.penup()
house_turtle.goto(-120, -180)
house_turtle.pendown()

sides_drawn = 0
while sides_drawn < 4:
    house_turtle.forward(240)
    house_turtle.left(90)
    sides_drawn = sides_drawn + 1

# Draw the triangle roof with a for loop.
# Facing right, the turtle draws the roof's base along the square's top.
house_turtle.penup()
house_turtle.goto(-120, 60)
house_turtle.pendown()

for side in range(3):
    house_turtle.forward(240)
    house_turtle.left(120)

house_turtle.hideturtle()
turtle.done()
