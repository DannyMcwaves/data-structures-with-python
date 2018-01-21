
__all__ = ["draw_triangle"]


import turtle
tl = turtle.Turtle()


def draw_triangle(*args):
    for i in args:
        tl.forward(i)
        tl.left(120)


def make_position(x, y):
    return None


def postionx(x):
    return None


def positiony(y):
    return None
