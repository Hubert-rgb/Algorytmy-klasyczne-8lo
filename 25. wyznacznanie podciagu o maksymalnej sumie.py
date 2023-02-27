def maxCiag(t):
    maxSuma = 0
    suma = 0
    for i in range(len(t)):
        if suma + t[i] > suma:
            suma += t[i]
        else:
            if suma > maxSuma:
                maxSuma = suma
            suma = 0
    return maxSuma

#jeśli aktualna suma ciągu po dodaniu konkretnego elementu jest mniejsza,
#to sprawdza, czy aktualna suma jest większa niż dotychczasowa największa suma
#potem rozpoczyna liczenie sumy od początku