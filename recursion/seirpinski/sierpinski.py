
__all__ = ["sierpinski"]
from .deps import trivial, mid, make_position
from .triangle import draw_triangle


def sierpinski(a, b, c):
    if trivial(a, b, c):
        return None

    # draw the triangle.
    draw_triangle(a, b, c)

    # define all the midpoints and recursively call the triangle
    ab = mid(a, b)
    bc = mid(b, c)
    ca = mid(c, a)
    print(ab, bc, ca)
    sierpinski(a, ab, ca)
    sierpinski(b, ab, bc)
    sierpinski(c, ca, bc)
    # return None

