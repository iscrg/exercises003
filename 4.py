def payment(p):
    if p <= 980:
        print('Успех!')
    else:
        print('Повторить попытку')


pay = int(input())
payment(pay)
