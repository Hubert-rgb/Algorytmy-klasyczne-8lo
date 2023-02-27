def dziel(t, n):
    d = [0 for i in range(len(t)//2 + 1)]
    m = [0 for i in range(len(t)//2 + 1)]

    for i in range(1, n, 2):
        if t[i] > t[i - 1]:
            d[i/2] = t[i]
            m[i/2] = t[i - 1]
        else:
            m[i / 2] = t[i]
            d[i / 2] = t[i - 1]
    if n %2 == 1:
