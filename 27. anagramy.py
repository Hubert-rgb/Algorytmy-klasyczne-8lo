def sklad(a):
    slownik = {}
    for x in a:
        try:
            slownik[x] += 1
        except:
            slownik[x] = 0
    return sorted(slownik)
def czyAnagramy(a, b):
    return sklad(a) == sklad(b)
print(czyAnagramy("niedziela", "dzielenia"))

#słowa składające się z tych samych liter
#dodaję do słownika każdą literę i ilość jej występowania
#sortuję słowniki i je porównuję