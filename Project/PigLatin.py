def pig_it(text):
    tokens = text.split(" ")
    output = " ".join(word[1:] + word[0] + "ay" if str(word).isalpha() else word for word in tokens)
    return output


print(pig_it("Hello world !"))
