#
# Calculates gaps in dataset
#


from datetime import datetime, timedelta


INPUT_FILE = '../data/closing_prices_all_per_day.txt'

with open(INPUT_FILE, 'r') as input:
    last_date = None

    for line in input:
        date, raw_date, raw_price, raw_volume = line.split(', ')

        date = datetime.fromtimestamp(int(raw_date)).date()
        
        if last_date:
            expected_date = last_date + timedelta(days=1)
            if date != expected_date:
                print('%s -> %s (%s days)' % (last_date, date, (date - last_date).days))

        last_date = date
