def days(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31

    elif month in [4, 6, 9, 11]:
        return 30

    elif month == 2:
        if ((year % 100 != 0 and year % 4 == 0) or
                (year % 400 != 0 and year % 100 == 0)):
            return 29
        else:
            return 28

def secbefore(date):
    date = date.split()
    date[0] = date[0].split('/')
    date[0] = list(map(int, date[0]))
    date[1] = date[1].split(':')
    date[1] = list(map(int, date[1]))
    
    res = 0

    res += date[1][2]
    res += date[1][1] * 60
    res += date[1][0] * 60**2

    res += date[0][1] * 60**2 * 24

    for i in range(1, date[0][0]):
        res += days(i, date[0][2]) * 60**2 * 24

    return res


# 11/19/2023 14:08:32
date = input()
print(secbefore(date))
