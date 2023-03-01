def sort(t):
    for i in range(len(t)):
        j = i
        while t[j - 1] > t[j] and j > 0:
            t[j], t[j - 1] = t[j - 1], t[j]
            j -= 1
    return t
print(sort([3, 6, 21, 21,7, 3, 8,3214]))