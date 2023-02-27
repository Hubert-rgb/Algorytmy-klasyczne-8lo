def sort(t):
    for j in range(len(t) - 1):
        i = 0
        while i < len(t) - j - 1:
            if t[i] > t[i + 1]:
                t[i], t[i + 1] = t[i + 1], t[i]
            i += 1
    return t
print(sort([3, 6, 2, 7, 7, 2, 8]))

#przeglada listę od początku i sprawdza czy element pierwszy jest większy od drugiego,
# jeśli tak to je zamienia i sprawdza czy drugi nie jest większy od 3 itd.
# jeśli nie jest to zostawia i sprawdza 2 z 3 itd.