def anagrams(word, words):
    output = list(str for str in words if sorted(str) == sorted(word))
    return output


anagrams("asd",["asd", "asd", "qweqw"])

