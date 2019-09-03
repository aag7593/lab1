"""
CSAPX Lab 1: Tiny Turtle

A program that takes an enhanced TT program, expands it into basic TT commands,
and then does turtle drawing from it.

author: Alexis Gordon
"""
import turtle


def evaluate(directions: str):
    if directions.index("I") != -1:
        directions = expand_iterate(directions)
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


def expand_iterate(instructions:str):
    start = instructions.index("I")
    end = instructions.index("@")
    repeat = instructions[start+3:end]
    times = int(instructions[start+1:start+2])
    new_instruct = ""
    for _ in range(0, times):
        new_instruct += repeat
    new_instruct = new_instruct[0:len(new_instruct)-1]
    return new_instruct


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
