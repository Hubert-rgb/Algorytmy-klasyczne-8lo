def dec2sys(x, system):
    cyfry = "0123456789ABCDEF"
    odwrocona = ""
    while x != 0:
        reszta = x % system
        odwrocona += cyfry[reszta]
        x //= system
    out = odwrocona[::-1]
    return out
print(dec2sys(80,16))

#dodaje resztę z dzielenia przez system
# (w odpowiednim zapisie w systemie, tablica cyfry potrzebna tylko w HEX)
# do odwróconej wersji odpowiedzi, następnie odwraca tą odpowiedź