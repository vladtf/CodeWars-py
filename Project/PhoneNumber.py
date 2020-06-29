def create_phone_number(n):
    strings = [str(x) for x in n]
    text = "".join(strings)
    output = "({0}) {1}-{2}".format(text[0:3], text[3:6], text[6:10])
    return output


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
