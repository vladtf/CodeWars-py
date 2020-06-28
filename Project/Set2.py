def get_middle(s):
    mid = int(len(s) / 2)
    return s[mid] + s[mid + 1] if len(s) % 2 == 0 else s[mid + 1]


def binary_array_to_number(arr):
    k = 2**(len(arr)-1)
    output = 0
    for x in arr:
        output += k * x
        k /= 2
    return output

binary_array_to_number([0,0,1,0])
