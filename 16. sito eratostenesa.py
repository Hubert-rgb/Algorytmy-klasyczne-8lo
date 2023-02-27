def erastotenes(n):
    t = []
    for i in range(n):
        t.append([i, True])
    i = 2
    while i < n:
        print(i)
        if t[i][1]:
            j = 2 * i
            while j < n:
                t[j][1] = False
                j += i
            i += 1
        else:
            i += 1
    return t
print(erastotenes(100))

#tworzę tablicę odpowiedzi z wartościami od 1 do n i wartością bool czy jest to liczba pierwsza (można zawsze dane zapisywać w inny sposób)
#bierze wartość liczby pierwszej (zaczynając od 2) i zamienia jej wielokrotności na FALSE (nie pierwsze)
#następnie sprawdza kolejną liczbę pierwszą (która wciąż ma TRUE)