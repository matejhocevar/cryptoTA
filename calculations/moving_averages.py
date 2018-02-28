#
# Simple Moving Average (SMA)
#


def sma(array, n=8):
    if not array or n < 1:
        return None
    return sum(array[-1*n:]) / float(n)


#
# Exponential Moving Average (EMA)
#

def ema(n=8, close=0, prev_ema=0):
    multiplier = 2 / (n + 1)
    return ((close - prev_ema) * multiplier) + prev_ema
