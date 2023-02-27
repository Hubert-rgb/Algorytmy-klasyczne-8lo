def czyPalindrom(a):
    odTylu = ""
    for i in range(len(a) - 1, -1, -1):
        odTylu += a[i]
    return odTylu == a
print(czyPalindrom("abcdba"))