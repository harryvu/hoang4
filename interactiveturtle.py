# we want to use turtle code
import turtle

# create the turtle
bob = turtle.Turtle()
bob.shape("turtle")

# infinite loop
while True:
    # ask for distance, move distance
    distance = input("How far will bob walk?")
    bob.forward(int(distance))

    # ask for angle, turn angle
    angle = input("How many degrees should bob turn?")
    bob.left(int(angle))
