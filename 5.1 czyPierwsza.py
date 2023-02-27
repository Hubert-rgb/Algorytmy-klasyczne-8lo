import math


def czyPierwsza(a):
    if a == 1:
        return False
    elif a == 2:
        return True
    else:
        counter = 0
        for i in range(2, int(math.sqrt(a) + 1)):
            if a % i == 0:
                counter += 1
        if counter == 0:
            return True
        return False
print(czyPierwsza(4))

#predefiniowane wartości dla 1 i 2
#sprawdza w pętli od 2 do pierwiastka z liczby zaokrąglonego w dół + 1,
# czy liczba jest podzielna przez iterrator,
# jeśli jest to nie jest pierwsza