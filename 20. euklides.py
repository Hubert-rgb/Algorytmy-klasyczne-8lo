def NWD_euklides(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
print(NWD_euklides(126, 189))

#algorytm do zapamiętania!!!