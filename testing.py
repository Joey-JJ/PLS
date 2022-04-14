import datetime as dt


date = dt.datetime.now().date()
format = '%d-%m-%Y'

# Converting to string
date_str = date.strftime(format)
# Converting to date object
date2 = dt.datetime.strptime(date_str, format).date()
print(date2)
