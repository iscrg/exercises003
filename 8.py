def converter(date):
    date = date.split()
    date[0] = date[0].split('/')
    date[0] = list(map(int, date[0]))
    date[1] = date[1].split(':')
    date[1] = list(map(int, date[1]))

    if date[0][0] > 12:
        exit()

    if date[0][0] in [1, 3, 5, 7, 8, 10, 12]:
        if date[0][1] > 31:
            exit()

    elif date[0][0] in [4, 6, 9, 11]:
        if date[0][0] > 30:
            exit()

    elif date[0][0] == 2:
        if ((date[0][2] % 100 != 0 and date[0][2] % 4 == 0) or
                (date[0][1] % 400 != 0 and date[0][2] % 100 == 0)):
            if date[0][1] > 29:
                exit()
        else:
            if date[0][1] > 28:
                exit()

    if date[1][0] > 24:
        exit()

    if date[1][1] > 59:
        exit()

    if date[1][2] > 59:
        exit()

    if date[1][0] > 12:
        date[1][0] -= 12
        date[1].append('PM')
    else:
        date[1].append('AM')

    res = '{day}.{month}.{year} {hr}:{min}:{sec} {ampm}'.format(day=date[0][1],
                                                                month=date[0][0],
                                                                year=date[0][2],
                                                                hr=date[1][0],
                                                                min=date[1][1],
                                                                sec=date[1][2],
                                                                ampm=date[1][3]
                                                                )

    print(res)


# 11/19/2023 14:08:32
date = input()
converter(date)
