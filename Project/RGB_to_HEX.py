def rgb(r, g, b):
    return to_hex255(r) + to_hex255(g) + to_hex255(b)


def to_hex255(x):
    return to_hex(norm(x) // 16) + to_hex(norm(x) % 16)


def to_hex(x):
    return str(x) if x <= 9 else chr(ord('A') + x - 10)


def norm(x):
    if x > 255:
        return 255
    return 0 if x < 0 else x


print(rgb(1, 2, 3))
