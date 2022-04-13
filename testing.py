import datetime


d1 = datetime.date.today()
d2 = datetime.date(2022, 4, 12)

a = datetime.date.strftime('20220312', '%d-%m-%Y')

print(a)
