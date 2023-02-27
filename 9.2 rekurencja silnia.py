def silnia(a):
    if a == 0:
        return 1
    elif a == 1:
        return 1
    else:
        return a * silnia(a - 1)
print(silnia(3))
