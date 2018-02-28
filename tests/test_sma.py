from calculations.moving_averages import sma


def test_sma_corner_cases():
    assert sma(None, None) is None
    assert sma([], None) is None
    assert sma([], 0) is None
    assert sma([], 1) is None
    assert sma([0], 1) == 0
    assert sma([1], 1) == 1
    assert sma([0, 0], 1) == 0
    assert sma([0, 0], 2) == 0
    assert sma([0, 1], 1) == 1
    assert sma([0, 0, 1], 1) == 1
    assert sma([0, 1, 0], 1) == 0


def test_sma_basic():
    assert sma([0, 1, 0], 2) == 0.5
    assert sma([1, 2, 3], 1) == 3
    assert sma([0, 3], 2) == 1.5
    assert sma([1, 2, 3], 1) == 3
    assert sma([1, 2, 3], 2) == 2.5
    assert sma([1, 2, 3], 3) == 2


def test_sma():
    assert sma([11, 12, 13, 14, 15], 5) == 13
    assert sma([12, 13, 14, 15, 16], 5) == 14
    assert sma([13, 14, 15, 16, 17], 5) == 15


def test_sma_advanced():
    assert sma([7.14, 6.95, 6.8, 6.6, 7.15, 6.2, 6.5, 6.0, 5.52, 6.28, 6.3, 6.79, 6.5, 6.52, 6.26], 8) != 6
