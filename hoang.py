import turtle

# define some global variables
window = turtle.Screen()
window.screensize(800, 600)
window.bgcolor("#EEEEEE")

turtle.speed(5)
turtle.pensize(2)
square_size = 50
number_of_blocks = 10
blocks_remain = 10


def draw_square(size, color='black'):
    cur_pos = turtle.pos()
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()


def above(n, color='black'):
    """ 
    Place a square the number of spaces above your current location
    and assign a color (default is black)
    """

    turtle.penup()
    cur_pos = turtle.pos()
    turtle.goto(cur_pos[0], cur_pos[1] + n * square_size)
    draw_square(square_size, color)


def below(n, color='black'):
    """ 
    Place a square the number of spaces below your current location
    and assign a color (default is black)
    """

    turtle.penup()
    cur_pos = turtle.pos()
    turtle.goto(cur_pos[0], cur_pos[1] - n * square_size)
    draw_square(square_size, color)


def right(n, color='black'):
    """ 
    Place a square the number of spaces right to your current location
    and assign a color (default is black)
    """

    turtle.penup()
    cur_pos = turtle.pos()
    turtle.goto(cur_pos[0] + n * square_size, cur_pos[1])
    draw_square(square_size, color)


def left(n, color='black'):
    """ 
    Place a square the number of spaces left to your current location
    and assign a color (default is black)
    """

    turtle.penup()
    cur_pos = turtle.pos()
    turtle.goto(cur_pos[0] - n * square_size, cur_pos[1])
    draw_square(square_size, color)


above(1, "yellow")
above(2, "red")
below(4, "green")
right(2, "blue")
left(5, "purple")
above(3)

# # create the turtle
# bob = turtle.Turtle()
# bob.shape("turtle")

# while True:
#     # ask for distance, move distance
#     distance = input("How far will bob walk?")
#     bob.forward(int(distance))

#     # ask for angle, turn angle
#     angle = input("How many degrees should bob turn?")
#     bob.left(int(angle))

while True:
    # ask for a command
    commandInput = input("Enter a command: .")
    argsStartIndex = commandInput.find('(')
    argsEndIndex = commandInput.find(')')
    command = commandInput[0:argsStartIndex]
    print(command)
    print(commandInput[argsStartIndex+1:argsEndIndex])

turtle.done()
