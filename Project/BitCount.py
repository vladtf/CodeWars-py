def count_bits(n):
    result = 0
    while n > 0:
        result += n % 2
        n //= 2
    return result

print(count_bits(7))