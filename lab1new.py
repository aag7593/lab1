"""
CSAPX Lab 1: Tiny Turtle

A program that takes an enhanced TT program, expands it into basic TT commands,
and then does turtle drawing from it.

author: Alexis Gordon
"""
import turtle

def evaluate(directions: str):
    commands = directions.split(" ")
    for string in commands:
        letter = string[0:1]
        if letter != "U" and letter != "D":
            num = int(string[1:4])
            if letter == "F":
                turtle.forward(num)
            elif letter == "B":
                turtle.backward(num)
            elif letter == "L":
                turtle.left(num)
            elif letter == "R":
                turtle.right(num)
            elif letter == "C":
                turtle.circle(num)
        elif letter == "U":
            turtle.up()
        elif letter == "D":
            turtle.down()


def main() -> None:
    evaluate(input("Enter your TT program directions"))
    turtle.mainloop()

    """
    The main function prompts the user to enter a TT program.  It then expands
    that program to the basic TT commands and then executes them.
    :return: None
    """

if __name__ == '__main__':
    main()
