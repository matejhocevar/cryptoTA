#
# Closing prices parser
# it takes ~ 1min to parse 21m+ lines
#
# bitstamp_all.csv downloaded from
# http://api.bitcoincharts.com/v1/csv/
#


from datetime import datetime


INPUT_FILE = '../data/bitstamp_all.csv'
# OUTPUT_FILE = '../data/closing_prices_all_per_day.txt'
OUTPUT_FILE = '../data/closing_prices_all_per_hour.txt'

with open(INPUT_FILE, 'r') as input:
    with open(OUTPUT_FILE, 'w') as output:
        
        last_date = None
        daily_volume = 0

        for line in input:
            raw_date, raw_price, raw_volume = line.split(',')

            # print('Date: %s | Price: %s | Volume: %s' % (raw_date, raw_price, raw_volume))

            date = datetime.fromtimestamp(int(raw_date))

            if last_date:
                if last_date.replace(minute=0, second=0, microsecond=0) != date.replace(minute=0, second=0, microsecond=0):
                    output.write('%s, %s, %s, %s\n' % (str(date), raw_date, raw_price, daily_volume))
                    daily_volume = 0

            last_date = date
            daily_volume += float(raw_volume)
