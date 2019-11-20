import turtle

window = turtle.Screen()
turtle.speed(5)
turtle.pensize(2)
# Draw the outline of a square
turtle.penup()
turtle.goto(-350, 100)
turtle.pendown()
turtle.color("blue")

turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.penup()

# Draw the outline of a square using a for Loop
turtle.goto(-200, 100)
turtle.color("red")
turtle.pendown()
for i in range(4):
    turtle.forward(150)
    turtle.left(90)
turtle.penup()

# Filled square with color
turtle.goto(-50, 100)
turtle.color("yellow")
turtle.pendown()
turtle.begin_fill()
for i in range(4):
    turtle.forward(150)
    turtle.left(90)
turtle.end_fill()

turtle.goto(100, 100)
turtle.color("green")
turtle.pendown()
turtle.begin_fill()
for i in range(4):
    turtle.forward(150)
    turtle.left(90)
turtle.end_fill()

turtle.goto(250, 100)
turtle.color("black")
turtle.pendown()
turtle.begin_fill()
for i in range(4):
    turtle.forward(150)
    turtle.left(90)
turtle.end_fill()

turtle.goto(250, -50), (100, -50)
turtle.color("purple", "pink")
turtle.pendown()
turtle.begin_fill()
for i in range(4):
    turtle.forward(150)
    turtle.left(90)
turtle.end_fill()


turtle.done()
