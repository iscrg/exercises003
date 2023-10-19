def nums(a, b):
    required = ['1', '3', '4', '8', '9']
    if b < a:
        a, b = (b, a)

    res = []

    for i in range(a, b+1):
        i = str(i)
        if any(num in i for num in required):
            res.append(i)

    print(*res)


a = int(input())
b = int(input())
nums(a, b)