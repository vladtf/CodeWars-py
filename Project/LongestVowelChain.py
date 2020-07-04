def solve(s):
    max_len = 0
    curr_len = 0
    for x in s:
        if x in "aeiou":
            curr_len += 1
            if curr_len > max_len:
                max_len = curr_len
        else:
            curr_len = 0

    return max_len
