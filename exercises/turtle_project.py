"""EX08 - Turtle Graphics: A surprising and daring return to Battleship!!"""

__author__: str = "730646830"

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()


def main() -> None:
    """The entrypoint of my scene."""
    MAX_SPEED: float = 0.5
    leo.speed(MAX_SPEED)
    ocean(leo, -320, -290)
    ocean_waves(leo, -320, -150)
    boat_structure(leo, -200, -50)
    windows(leo, -90, -60)
    mast_and_flag(leo, -10, 170)
    done()


def ocean(mike: Turtle, x: float, y: float) -> None:
    """Draws a ocean."""
    mike = leo
    turn: int = 90
    mike.penup()
    mike.goto(x, y)
    mike.pendown()
    mike.pencolor("blue")
    mike.color("blue")
    mike.begin_fill()
    i: int = 0
    while (i < 4):
        if i % 2 == 0:
            mike.forward(700)
            mike.left(turn)
        else: 
            mike.forward(200)
            mike.left(turn)
        i += 1
    mike.end_fill()


def ocean_waves(mike: Turtle, x: float, y: float) -> None:
    """Makes motion lines in the ocean."""
    mike = leo
    mike.penup()
    mike.goto(x, y)
    mike.pendown()
    mike.color("white")
    i: int = 0
    while i < 16:
        if i <= 7: 
            a: float = x + (110 * i)
            mike.forward(20)
            mike.left(30)
            mike.forward(20)
            mike.right(30)
            mike.forward(20)
            mike.right(30)
            mike.forward(20)
            mike.left(30)
            mike.forward(20)
            mike.penup()
            mike.goto(a, y)
            mike.pendown()
            i += 1
        else: 
            b: float = (x - 40) + (110 * (i - 8))
            mike.forward(20)
            mike.left(30)
            mike.forward(20)
            mike.right(30)
            mike.forward(20)
            mike.right(30)
            mike.forward(20)
            mike.left(30)
            mike.forward(20)
            mike.penup()
            mike.goto(b, y - 60)
            mike.pendown()
            i += 1


def boat_structure(mike: Turtle, x: float, y: float) -> None:
    """Draw that boat!"""
    mike = leo
    mike.penup()
    mike.goto(x, y)
    mike.pendown()
    colormode(255)
    mike.color("red")
    mike.begin_fill()
    mike.right(50)
    mike.forward(150)
    mike.left(50)
    mike.forward(250)
    mike.left(50)
    mike.forward(150)
    mike.left(40)
    mike.forward(20)
    mike.left(90)
    mike.forward(479.813)
    mike.left(90)
    mike.forward(20)
    mike.end_fill()
    

def windows(mike: Turtle, x: float, y: float) -> None:
    """Makes the windows of the boat."""
    mike = leo
    i: int = 0
    mike.penup()
    mike.goto(x, y)
    mike.color("white")
    mike.begin_fill()
    while i < 3:
        a: float = x + (80 * i)
        mike.penup()
        mike.goto(a, y)
        mike.pendown()
        o: int = 0
        while o < 4:
            if o % 2 == 0:
                mike.forward(40)
                mike.left(90)
            else: 
                mike.forward(40)
                mike.left(90)
            o += 1
        i += 1
    mike.end_fill()


def mast_and_flag(mike: Turtle, x: float, y: float) -> None:
    """Raise the flag!"""
    mike = leo
    mike.penup()
    mike.goto(x, y)
    mike.pendown()
    mike.color("brown")
    mike.begin_fill()
    i: int = 0
    while i < 4:
        if i % 2 == 0:
            mike.forward(200)
            mike.left(90)
        else: 
            mike.forward(20)
            mike.left(90)
        i += 1
    mike.end_fill()
    mike.left(90)
    mike.forward(20)
    mike.color("yellow")
    mike.begin_fill()
    mike.right(45)
    mike.forward(125)
    mike.right(90)
    mike.forward(125)
    mike.end_fill()


if __name__ == "__main__": 
    main()