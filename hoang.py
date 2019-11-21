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


command_dict = {
    'above': above,
    'below': below,
    'right': right,
    'left': left
}

while True:
    # ask for a command
    commandInput = input("Enter a command: >").replace(" ", "")

    # construct the command
    argsStartIndex = commandInput.find('(')
    argsEndIndex = commandInput.find(')')
    command = commandInput[0:argsStartIndex]
    if command in command_dict.keys():
        commandArgs = commandInput[argsStartIndex+1:argsEndIndex].split(',')
        print(commandArgs)

        if len(commandArgs) > 1:
            n = int(commandArgs[0])
            color_name = commandArgs[1]
        else:
            n = int(commandArgs[0])
            color_name = "black"

        # execute the command
        command_dict[command](n, color_name)
    else:
        print("Sorry, I don't understand!")
        # show_instruction()


turtle.done()
