def zero(x=None):
    if x is not None:
        return x(0)
    return 0


def one(x=None):
    if x is not None:
        return x(1)
    return 1


def two(x=None):
    if x is not None:
        return x(2)
    return 2


def three(x=None):
    if x is not None:
        return x(3)
    return 3


def four(x=None):
    if x is not None:
        return x(4)
    return 4


def five(x=None):
    if x is not None:
        return x(5)
    return 5


def six(x=None):
    if x is not None:
        return x(6)
    return 6


def seven(x=None):
    if x is not None:
        return x(7)
    return 7


def eight(x=None):
    if x is not None:
        return x(8)
    return 8


def nine(x=None):
    if x is not None:
        return x(9)
    return 9


def plus(x): return lambda y: y + x


def minus(x): return lambda y: y - x


def times(x): return lambda y: y * x


def divided_by(x): return lambda y: y // x


print(one(plus(one())))
