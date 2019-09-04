"""
CSAPX Lab 1: Tiny Turtle

A program that takes an enhanced TT program, expands it into basic TT commands,
and then does turtle drawing from it.

author: Alexis Gordon
"""
import turtle


def evaluate(directions: str):
    if directions.find("P") != -1:
        directions = expand_polygon(directions)
    if directions.find("I") != -1:
        directions = expand_iterate(directions)
    commands = directions.split(" ")
    for string in commands:
        letter = string[0:1]
        if letter != "U" and letter != "D":
            num = float(string[1:])
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


def expand_iterate(instructions: str):
    start = instructions.index("I")
    finish = instructions.index("@")
    repeat = instructions[start+3:finish]
    times = int(instructions[start+1:start+2])
    new_instruct = ""
    beg = ""
    end = ""
    if instructions[0] != "I":
        beg = instructions[0:start]
    if instructions[len(instructions)-1:len(instructions)] != "@":
        end = instructions[finish+1:]
    for _ in range(0, times):
        new_instruct += repeat
    new_instruct = beg + new_instruct[0:len(new_instruct)-1] + end
    return new_instruct


def expand_polygon(instructions: str):
    p = instructions.index("P")
    sides = int(instructions[p + 1:p + 2])
    angle = 360 / sides
    length = int(instructions[p + 3:p + 6])
    beg = ""
    end = ""
    if p != 0:
        beg = instructions[0:p]
    elif len(instructions) != 6:
        end = instructions[p+6:]
    new_instruct = beg + "I" + str(sides) + " F" + str(length) + " L" + str(angle) + " @" + end
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
