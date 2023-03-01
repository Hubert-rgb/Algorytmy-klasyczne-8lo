def sort(t, lewy, prawy):
    if lewy < prawy:
        pivotIndex = Podziel(t, lewy, prawy)
        sort(t, lewy, pivotIndex - 1)
        sort(t, pivotIndex + 1, prawy)
def Podziel(t, pivotIndex, prawy):
    pivot = t[pivotIndex]
    lewy = pivotIndex
    for i in range(lewy, prawy):
        if t[i] < pivot:
            t[i], t[lewy] = t[lewy], t[i]
            lewy += 1
    #t[pivotIndex], t[lewy] = t[lewy], t[pivotIndex]
    return pivotIndex
t = [3, 6, 21, 223,7, 13, 8,3214]
sort(t, 0, len(t))
print(t)

#jakoś działa a chyba nie powinno