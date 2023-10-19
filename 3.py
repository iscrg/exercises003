def cost(price, holiday, loyalty_card):
    ratio = 1

    if holiday:
        ratio -= 0.03

    if loyalty_card:
        ratio -= 0.05

    if price >= 30000:
        ratio -= 0.1
    elif price >= 20000:
        ratio -= 0.07
    elif price >= 15000:
        ratio -= 0.05
    elif price >= 5000:
        ratio -= 0.03

    if ratio <= 0.85:
        ratio = 0.85

    finaly_price = price * ratio
    finaly_price = round(finaly_price, 2)

    return finaly_price


price = int(input('Type in the price: '))
holiday = bool(input('Is there a holiday on this day? [0 / 1]'))
loyalty_card = bool(input('Is there a loyalty card? [0 / 1]'))

print(cost(price, holiday, loyalty_card))
