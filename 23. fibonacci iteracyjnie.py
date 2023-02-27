def fibonacciIteracyjnie(n):
    t = []
    t.append(0)
    t.append(1)
    for i in range(2, n):
        t[i] = t[i - 1] + t[i - 2]
    return t[n - 1]

#tworzy tablicę w której zapisuje każdy dotychczas oblicony element ciągu i na jej podstawie liczy kolejne