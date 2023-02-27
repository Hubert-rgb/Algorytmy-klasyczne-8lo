def czynniki(x):
    t = []
    while x > 1:
        i = 2
        while x % i != 0:
            i += 1
        t.append(i)
        x //= i
    return t
print(czynniki(126))

#sprawdza czy liczba jest podzielna przez 2 < czynnik < liczby
#jeśli tak to dodaje do tablicy czynników i dzieli całkowicie przez tą liczbę
#jeśli nie to iteruje dalej