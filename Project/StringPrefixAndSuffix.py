def solve(st):
    i = 1
    max_len = 0
    st_rev = st[::-1]
    try:
        while i <= len(st) // 2:
            if st_rev.index(st[:i][::-1]) == 0:
                max_len = i
            i += 1
    finally:
        return max_len


print(solve("abcd"))
