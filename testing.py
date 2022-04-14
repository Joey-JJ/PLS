import datetime as dt


date = dt.datetime.now()
format = '%d%m%Y-%H%M%S'

# Converting to string
date_str = date.strftime(format)

# Converting to date object
# date2 = dt.datetime.strptime(date_str, format).date()

print(date_str)
