def phone_card(price):
    if price in [5, 10]:
        return price
    if price == 25:
        return price + 3
    elif price == 50:
        return  price + 8
    elif price == 100:
        return price + 20

    return None


price = int(input('Type in the price:'))
print(phone_card(price))
