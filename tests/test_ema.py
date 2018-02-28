from calculations.moving_averages import ema


def test_ema_corner_cases():
    assert ema(0, 0, 0) == 0
    assert ema(1, 0, 0) == 0
    assert ema(2, 0, 0) == 0


def test_ema_basic():
    assert ema(0, 1, 0) == 2
    assert ema(0, 5, 0) == 10
    assert ema(0, 10, 0) == 20
