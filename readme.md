# Crypto Technical Analysis Simulator

Crypto TA simulator written in Python.
Scope of this project is to test different TA strategies on crypto dataset.

## TA Strategies implemented
* SMA
* EMA

## Prerequisites
	virtualenv
	pip

## Installation
	git clone https://github.com/matoxxx/cryptoTA.git


Navigate to:

	cd cryptoTA

##### Activate virtual enviroment
on Windows:

	cd env/Scripts
	activate

on Unix:

	source env/bin/activate

##### Install dependencies:
	pip install -r requirements.txt

## Parsing data
* use existing datasets from `data` directory
* or download your own dataset from [bitcoincharts.com](http://api.bitcoincharts.com/v1/csv/) and save it in `data` directory

Navigate to parsers

    cd parsers

Modify `closing_prices.py` to your needs and run it

    python closing_prices.py

## Usage

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

or

    python run.py

## Tests
Run unit tests with

    pytest

### Author
Matej Hocevar [@matoxxx](https://github.com/matoxxx)