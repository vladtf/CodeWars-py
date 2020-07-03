from itertools import groupby


def duplicate_count(text):
    k = 0
    text = text.lower()
    text = list(text)
    text.sort()
    key_f = lambda x: x
    for key, group in groupby(text, key_f):
        if len(list(group)) > 1:
            k += 1
    return k


print(duplicate_count("indivisibility"))
