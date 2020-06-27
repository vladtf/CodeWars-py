import numpy


def spin_words(sentence):
    words = sentence.split(" ")
    output = ""
    for word in words:
        aux = word
        if len(word) > 4:
            aux = ""
            while len(word) > 0:
                aux = word[0] + aux
                word = word[1:]
        output += aux + " "

    output = output[:-1]
    return output


# print(spin_words("Welcome is"))

def find_outlier(integers):
    oddity = 1 if integers[0] % 2 + integers[1] % 2 + integers[2] % 2 < 2 else 0
    return [x for x in integers if x % 2 == oddity][0]


print(find_outlier([1, 2, 3]))
