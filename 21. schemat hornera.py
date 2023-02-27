def horner(wspolczynniki, dzielnik):
    wynik = 0
    for i in range(len(wspolczynniki)):
        wynik = wynik * dzielnik + wspolczynniki[i]
    return wynik
print(horner([2, -5, 4, -1], 1))

#po prostu to co na matmie