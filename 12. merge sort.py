#rekurencja devide and conquer
def sort(t):
    #bez tego będzie reqursive error
    if len(t) == 1:
        return t

    srodek = len(t) // 2
    #devide
    t1 = t[:srodek]
    t2 = t[srodek:]

    t1 = sort(t1)
    t2 = sort(t2)

    return merge(t1, t2)
#conquer
def merge(t1, t2):
    tOut = []
    #dołanczanie elementów lepszych(mniejszych)
    while len(t1) > 0 and len(t2) > 0:
        if t1[0] > t2[0]:
            tOut.append(t2[0])
            t2.pop(0)
        else:
            tOut.append(t1[0])
            t1.pop(0)
    #dołanczanie pozostałych elementów
    while len(t1) > 0:
        tOut.append(t1[0])
        t1.pop(0)
    while len(t2) > 0:
        tOut.append(t2[0])
        t2.pop(0)
    return tOut
print(sort([3, 6, 21, 21,7, 3, 8,3214]))
