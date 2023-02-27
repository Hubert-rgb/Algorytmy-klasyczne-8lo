def pochodna(wspolczynniki):
    pochodnaArr = []
    for i in range(len(wspolczynniki) - 1):
        stopien = len(wspolczynniki) - i - 1
        pochodnaLiczby = stopien * wspolczynniki[i]
        pochodnaArr.append(pochodnaLiczby)
    return pochodnaArr
print(pochodna([2, 2, 6, 10, -4]))

#wzorki z matmy (chyba też miało byc chornerem, ale nie wiem jak to zrobić)