import turtle
import sys

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

def colors():
    print(avail_colors)

def exit():
    """exit the program"""
    sys.exit()

avail_colors = ['black','white','cyan','magenta','yellow','red','green','blue','purple','orange','brown','gold','teal']

command_dict = {
    'above': above,
    'below': below,
    'right': right,
    'left': left,
    'colors': colors,
    'exit': exit
}

while True:
    # ask user to input a command
    commandInput = input("Enter a command: >").replace(" ", "")

    # construct the command
    argsStartIndex = commandInput.find('(')
    argsEndIndex = commandInput.find(')')
    command = commandInput[0:argsStartIndex]
    commandArgsString = commandInput[argsStartIndex+1:argsEndIndex]
    
    if command not in command_dict.keys():
        print("Wrong command!")
        continue
    else:
        # validate command arguments
        if commandArgsString == '':
            if "exit" in command:
                exit()
            elif "colors" in command:
                colors()
                continue
        else:          
            commandArgs = commandArgsString.split(',')
    
            if len(commandArgs) == 2:
                n = int(commandArgs[0])
                color_name=commandArgs[1]
                if color_name not in avail_colors:
                    print("Available colors are:")
                    colors()
                    continue
            else:
                n=int(commandArgs[0])
                color_name="black" # black is the default color

            # execute the command
            command_dict[command](n, color_name)

turtle.done()
