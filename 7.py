def dividers(a, b, n):
    res = []
    for i in range(1, n+1):
        if a % i == 0 and b % i == 0:
            res.append(i)

    return res


a = int(input('Type in A: '))
b = int(input('Type in B: '))
n = int(input('Type in N: '))

print(dividers(a, b, n))
