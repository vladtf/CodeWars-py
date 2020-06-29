def likes(names):
    length = len(names)
    cases = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
    }
    output = cases[min(4, length)].format(*names, others=length-2)
    return output


print(likes(['Alex', 'Jacob', 'Mark', 'Max']))


# def likes(*names):
#     if len(names) < 2:
#         name = "no one" if len(names) == 0 else names[0]
#         return name + " like this"
#
#     text = names[0]
#     if len(names) == 2:
#         text += " and " + names[1]
#     elif len(names) == 3:
#         text += ", " + names[1] + " and " + names[2]
#     else:
#         text += ", " + names[1] + " and " + str(len(names) - 2) + " others"
#
#     return text + " like this"
