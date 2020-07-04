def solve(st):
    output = min(st)
    max_len = 0
    for x in st:
        if st.count(x) < 2:
            continue

        length = chr_value(st, x)
        if length > max_len:
            output = x
            max_len = length
        elif length == max_len:
            output = chr(min(ord(x), ord(output)))

    return output


def chr_value(st, x):
    st_index = st.index(x)
    end_index = len(st) - st[::-1].index(x) - 1
    length = abs(st_index - end_index)
    return length


# def solve(st):
#     return max((st.find(c) - st.rfind(c),c) for c in list(st))


print(solve("bcd"))
