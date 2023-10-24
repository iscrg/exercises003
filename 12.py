import turtle


def circle(trtl, radius, fill_color):
    trtl.fillcolor(fill_color)
    trtl.begin_fill()
    trtl.circle(radius)
    trtl.end_fill()


def square(trtl, side, fill_color):
    trtl.fillcolor(fill_color)
    trtl.begin_fill()
    for _ in range(4):
        trtl.forward(side)
        trtl.right(90)
    trtl.end_fill()


def triangle(trtl, side, fill_color):
    trtl.fillcolor(fill_color)
    trtl.begin_fill()
    for _ in range(2):
        trtl.forward(side)
        trtl.right(90)
    trtl.right(45)
    trtl.end_fill()

    hypotenuse = (side**2 + side**2) ** 0.5
    trtl.forward(hypotenuse)


def draw():
    colors = [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "purple",
        "pink",
        "brown",
        "gray",
        "black",
    ]

    trtl = turtle.Turtle()

    trtl.left(90)
    square(trtl, 100, colors[0])
    trtl.left(90)
    square(trtl, 100, colors[1])
    trtl.left(90)
    square(trtl, 100, colors[2])
    trtl.left(90)
    square(trtl, 100, colors[3])

    trtl.right(90)
    trtl.forward(100)
    trtl.left(90)

    trtl.right(180)
    triangle(trtl, 100, colors[1])

    trtl.left(45)

    for i in range(9, 0, -1):
        circle(trtl, 10*i, colors[i])

    turtle.done()


draw()
