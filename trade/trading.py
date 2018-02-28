

def buy(price, fiat):
    if price <= 0:
        return 0
    return fiat / float(price)


def sell(price, coins):
    return price * coins


def place_buy_order(price, coins, fiat):
    fiat_balance = fiat
    coins_balance = coins

    if fiat_balance <= 0:
        return coins_balance, fiat_balance, False
    else:
        coins_balance = buy(price, fiat)
        fiat_balance = 0

    return coins_balance, fiat_balance, True


def place_sell_order(price, coins, fiat):
    fiat_balance = fiat
    coins_balance = coins

    if coins_balance <= 0:
        return coins_balance, fiat_balance, False
    else:
        fiat_balance = sell(price, coins)
        coins_balance = 0

    return coins_balance, fiat_balance, True