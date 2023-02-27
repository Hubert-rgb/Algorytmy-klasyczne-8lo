def sort(t):
    for i in range(len(t)):
        minIndex = i
        for j in range(i, len(t)):
            if t[j] < t[minIndex]:
                minIndex = j
        #swap values
        t[i], t[minIndex] = t[minIndex], t[i]
    return t
print(sort([1, 43, 23, 6, 3, 6, 7]))

#przegląda cąłą tablicę i szuka index wartości najmniejszej,
#następnie podmienia wartości najmniejszej i index 0 itd. (tylko od następnej iteracji od następnej wartości [index = 1itd.])