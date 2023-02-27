def fiboncacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fiboncacci(n - 1) + fiboncacci(n - 2)
print(fiboncacci(6))

#F(x) = 0 dla x = 0
#       1 dla x = 1
#       f(x - 1) + f(x - 2)