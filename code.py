# Enter the coin you wish to buy
coin = 'ksm'
# Enter the USDT amount you want to buy
amount = 100000000
# Enter whether your buying or selling
sell_or_buy = 'buy'

AMOUNT = amount


men = 0

def add_coma_remove_coma(value):
    # remove full stop
    value1 = ''
    value = str(value)
    for i in value:
        if i != '.':
            value1 += i
        else:
            break
    value = value1
    # add comas
    value = format(int(value), ",")
    return value

while men == 0:
    from kucoin.client import Client
    # Enter kucoin api keys
    API_SECRET_KEY = ""
    API_PUBLIC_KEY = ""
    PASSPHRASE = ""
    client = Client(API_PUBLIC_KEY, API_SECRET_KEY, PASSPHRASE)

    if sell_or_buy == 'buy':
        sell_or_buy1 = 'asks'
    else:
        sell_or_buy1 = 'bids'


    kucoin_order_book = client.get_full_order_book("{}-USDT".format(coin.upper()))
    kucoin_order_book = kucoin_order_book[sell_or_buy1]

    ####

    amount1 = amount

    buy_prices = []
    dollar_amounts_brought = []

    for i in kucoin_order_book:
        dollar_amount = float(i[0]) * float(i[1])
        if dollar_amount > amount1:
            buy_prices.append(i[0])
            dollar_amounts_brought.append(amount1)
            break
        else:
            amount1 = amount1 - dollar_amount
            buy_prices.append(i[0])
            dollar_amounts_brought.append(dollar_amount)


    coin_buy_amount = 0

    for index, i in enumerate(dollar_amounts_brought):
        brought_amount = float(i) / float(buy_prices[index])
        coin_buy_amount += float(brought_amount)

    current_price = str(client.get_ticker('{}-USDT'.format(coin.upper()))['price'])



    famount = add_coma_remove_coma(amount)
    fcoin_buy_amount = add_coma_remove_coma(coin_buy_amount)

    print('You would spend ${} on {} KMA which would cost a average of ${}, the current price is {}'.format(famount, fcoin_buy_amount, amount / coin_buy_amount, current_price))
    yesNo = input('Type \'B\' to buy and enter to receive another quote : ')

    print('\n')

    if yesNo == 'B':
        men += 1
        order_coin = coin.upper() + "-USDT"
        the_order = client.create_market_order(order_coin, Client.SIDE_BUY, funds=str(AMOUNT))
        order_id = the_order['orderId']
        order_id = client.get_order(order_id)
        coins_purchased = order_id['dealSize']
        USDT_purchased = order_id['dealFunds']
        symbol = order_id['symbol']
        cost = float(USDT_purchased) / float(coins_purchased)
        print('\n')
        print('-' * 140)
        print('You purchased {} of {} which cost ${} and a buy price of ${}'.format(coins_purchased, symbol, USDT_purchased, cost))
        print('-' * 140)
