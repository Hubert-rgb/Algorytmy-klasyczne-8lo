#szyfrowanie równoległe, więc klucz jest NIEjawny

def szyfruj(tekst, klucz):
    #przygotowanie tabeli
    dlugosc = len(tekst)
    tab = [[0 for x in range(dlugosc)] for y in range(klucz)]
    y = 0
    yWDol = True
    x = 0
    #wpisanie do tabeli według szyfru
    for i in range(len(tekst)):
        tab[y][x] = tekst[i]
        x += 1
        if yWDol:
            if y + 1 == klucz:
                yWDol = False
                y -= 1
            else:
                y += 1
        else:
            if y - 1 >= 0:
                y-=1
            else:
                yWDol = True
                y += 1
    #odczytanie szyfru
    odczyt = ""
    for y in range(klucz):
        for x in range(len(tekst)):
            if tab[y][x] != 0:
                odczyt += tab[y][x]
    return odczyt

print(szyfruj("abecadlo", 3))

#tablica 2 wymiarowa o długości wyrazu i wysokości klucza
#dodaje kolejne znaki tekstu we wzór zyg-zag (w dół i prawo do samego dołu i z powrotem do góry)
#oczytuje elementy od lewej do prawej, od góry do dołu