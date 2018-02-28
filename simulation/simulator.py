from datetime import datetime
import os

from calculations.moving_averages import sma, ema
from trade import trading
from utils.enum import Enum

DIR = os.path.dirname(__file__)
INPUT_FILE = '../data/closing_prices_all_per_hour.txt'

Signal = Enum(['BUY', 'SELL', 'HODL'])


class Simulator:
    coins = None
    fiat = None
    prices = []

    ema1_n = None
    ema2_n = None

    from_date = datetime.strptime('2012-01-11', '%Y-%m-%d').date()
    to_date = datetime.now().date()

    display_orders = False

    def __init__(self, from_date=None, to_date=None, starting_coins=1.00, starting_fiat=0, ema1=8, ema2=13, display_orders=False):
        print('=' * 80)
        self.from_date = datetime.strptime(from_date, '%Y-%m-%d').date() if from_date else self.from_date
        self.to_date = datetime.strptime(to_date, '%Y-%m-%d').date() if to_date else self.to_date
        print('[-] Simulating from %s to %s (inclusive)' % (self.from_date, self.to_date))
        self.display_orders = display_orders
        print('[-] %-20s: %s' % ('Displaying orders', self.display_orders))

        self.ema1_n = ema1
        self.ema2_n = ema2
        print('[-] %-20s: %d' % ('First EMA value', self.ema1_n))
        print('[-] %-20s: %d' % ('Second EMA value', self.ema2_n))

        self.load_prices()
        print('[-] %-20s: %d ' % ('Prices loaded:', len(self.prices)))

        self.coins = starting_coins
        print('[-] %-20s: %f' % ('Initial coin amount', self.coins))
        self.fiat = starting_fiat
        print('[-] %-20s: %f' % ('Initial fiat amount', self.fiat))
        print('[-] %-20s: %f' % ('Initial value', self.get_fiat_balance(self.prices[0])))

        print('[-] Starting simulation...')
        print('=' * 80)
        self.simulateEMA()

    def load_prices(self):
        file_path = os.path.join(DIR, INPUT_FILE)
        with open(file_path) as file:
            for line in file:
                date, raw_date, raw_price, raw_volume = line.split(',')
                date = datetime.fromtimestamp(int(raw_date)).date()

                if self.from_date <= date <= self.to_date:
                    self.prices.append(float(raw_price))

    def get_prices(self, from_id=None, to_id=None):
        if not from_id and not to_id:
            return self.prices
        if not to_id:
            return self.prices[from_id:]
        if not from_id:
            return self.prices[:to_id]
        return self.prices[from_id:to_id]

    def get_balance(self, price):
        return self.coins + self.fiat / float(price)

    def get_fiat_balance(self, price):
        return self.get_balance(price) * price

    def simulateEMA(self):
        start_id = self.ema2_n
        initial_sma_1 = sma(self.prices[:start_id], self.ema1_n)
        initial_sma_2 = sma(self.prices[:start_id], self.ema2_n)

        prev_ema1 = initial_sma_1
        prev_ema2 = initial_sma_2

        last_signal = Signal.HODL
        last_price = None

        for closing_price in self.prices[start_id:]:
            ema1 = ema(self.ema1_n, closing_price, prev_ema1)
            ema2 = ema(self.ema2_n, closing_price, prev_ema2)

            if ema1 > ema2:
                signal = Signal.BUY
            else:
                signal = Signal.SELL

            if last_signal != signal:
                order_completed = False

                if signal == Signal.BUY:
                    self.coins, self.fiat, order_completed = trading.place_buy_order(
                        price=closing_price,
                        coins=self.coins,
                        fiat=self.fiat
                    )
                elif signal == Signal.SELL:
                    self.coins, self.fiat, order_completed = trading.place_sell_order(
                        price=closing_price,
                        coins=self.coins,
                        fiat=self.fiat
                    )

                if order_completed and self.display_orders:
                    print('%s,%f,%f,%f,%f' % (signal, closing_price, self.coins, self.fiat, self.get_balance(self.prices[start_id])))

            prev_ema1 = ema1
            prev_ema2 = ema2
            last_signal = signal
            last_price = closing_price

        remaining_coins = trading.buy(last_price, self.fiat)
        print('=' * 80)
        print('[-] %-20s: %f' % ('Coin amount', self.coins))
        print('[-] %-20s: %f (%f coins)' % ('Fiat amount', self.fiat, remaining_coins))
        print('-' * 80)
        print('[-] %-20s: %f [!]' % ('Final coin amount', self.get_balance(last_price)))
        print('[-] %-20s: %f' % ('Final value', self.get_fiat_balance(last_price)))
        print('=' * 80)
