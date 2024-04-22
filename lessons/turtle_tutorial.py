from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.forward(50)
leo.left(30)
leo.right(40)

leo.begin_fill()
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.end_fill()

i: int = 0
while (i < 4):
    leo.forward(300)
    leo.left(90)
    i = i + 1

leo.penup()
leo.goto(45, 60)
leo.pendown()

i: int = 0
while (i < 3):
    leo.begin_fill()
    leo.forward(300)
    leo.left(120)
    leo.end_fill()
    i = i + 1

leo.goto(45, 60)
leo.color("blue")
colormode(255)
leo.color(99, 204, 250)

leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.color("green", "yellow")

side_length: int = 230

i: int = 0
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i = i + 1

done()