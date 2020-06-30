def nb_dig(n, d):
    k = 0
    i = 1
    while i * i <= n * n:
        if str(d) in str(i):
            k += 1
        i += 1
    return k


print(nb_dig(5750, 0))
