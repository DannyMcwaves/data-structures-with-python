
__all__ = ["mid", "trivial"]


def trivial(*args):
    if sum(args) < 5:
        return True
    return False


def mid(x, y):
    return (x + y) / 2

