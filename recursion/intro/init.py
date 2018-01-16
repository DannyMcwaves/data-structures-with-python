# this is just the start of me trying to learn
# recursions and all that should come with it along the way.
# Introduction o recursion

import turtle


def upAndMove(t:turtle.Turtle, length):
    t.up()
    t.forward(length)
    t.down()


def fractalMovement(t, size):
    if size == 0:
        return None
    t.forward(size/3)
    t.left(60)
    t.forward(size/3)
    t.right(120)
    t.forward(size/3)
    t.left(60)
    t.forward(size/3)
    fractalMovement(t, size-10)


def fractal(t:turtle.Turtle, size, order):
    """
    :param t: turtle
    :param size: the size of the line
    :param order: the smallest level of the fractal
    :return: None
    """
    # t.forward(size/3)
    if order == 0:
        t.forward(size)
        t.up()
        t.goto(0, 0)
    else:
        fractal(t, size/3, order-1)
        t.left(60)
        fractal(t, size/3, order-1)
        t.right(120)
        fractal(t, size/3, order-1)
        t.left(60)
        fractal(t, size/3, order-1)


turl = turtle.Turtle()
size = 300
upAndMove(turl, -size/2)
fractal(turl, size, 5)

ts = turl.getscreen()
turtle.done()
