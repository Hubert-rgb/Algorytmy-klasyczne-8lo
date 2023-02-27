def sumyPrefiksowe(t):
    sumy = [0]
    for i in range(1, len(t) + 1):
        sumy.append(sumy[i - 1] + t[i - 1])
    return sumy
print(sumyPrefiksowe([18, 11, 6, -2, 12, -19]))

#tworzy tablicę z obliczonymi wartościami sumy do aktualnego elementu tablicy