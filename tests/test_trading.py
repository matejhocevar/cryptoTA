from trade.trading import buy, sell


def test_buy():
    assert buy(0, 0) == 0
    assert buy(1, 0) == 0
    assert buy(10, 0) == 0
    assert buy(100, 0) == 0
    assert buy(0, 1) == 0
    assert buy(0, 10) == 0
    assert buy(0, 100) == 0

    assert buy(1, 100) == 100
    assert buy(10, 100) == 10
    assert buy(100, 100) == 1
    assert buy(1000, 100) == 0.1
    assert buy(1000, 10) == 0.01


def test_sell():
    assert sell(0, 0) == 0
    assert sell(1, 0) == 0
    assert sell(10, 0) == 0
    assert sell(100, 0) == 0
    assert sell(0, 1) == 0
    assert sell(0, 10) == 0
    assert sell(0, 100) == 0

    assert sell(1, 100) == 100
    assert sell(1, 1000) == 1000
    assert sell(10, 1000) == 10000
    assert sell(10, 100) == 1000
    assert sell(100, 100) == 10000
    assert sell(1000, 1000) == 1000000