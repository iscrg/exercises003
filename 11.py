def is_simple(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def crunching(n):
    for i in range(1, n+1):
        if is_simple(i):
            print(i)


n = int(input())
crunching(n)
