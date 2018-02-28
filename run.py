from simulation.simulator import Simulator

s = Simulator(
    from_date='2014-01-01',
    to_date='2015-01-01',
    starting_fiat=0,
    starting_coins=1,
    ema1=8,
    ema2=13,
    display_orders=False
)
