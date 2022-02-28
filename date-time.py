import datetime
import pytz


d = datetime.date(2022, 2, 19)
print(d)

tday = datetime.date.today()
# monday=0 sunday=6
print(tday.weekday())
# monday=1 sunday=7
print(tday.isoweekday())

tdelta = datetime.timedelta(days=7)
print(tday + tdelta)
print(tday - tdelta)

# date2 = date1 + timedelta
# date2timedleta = date1 + date2

bday = datetime.date(1999, 3, 10)
till_bday = tday - bday
print(till_bday.days)

t = datetime.time(9, 30, 45)
print(t)

# current local time
dt_today = datetime.datetime.today()
# can pass timezone
dt_now = datetime.datetime.now()
# current utc time
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

# pip install pytz
# python doc also recommand pytz
dt = datetime.datetime(2022, 2, 19, 9, 30, 54, tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_bdtz = dt_now.astimezone(pytz.timezone("Asia/Dhaka"))
print(dt_bdtz)

# list all timezone
for tz in pytz.all_timezones:
    print(tz)


# strftime - Datetime to String
# strptime - String to Datetime
dt = datetime.datetime.now(tz=pytz.timezone("Asia/Dhaka"))
dt_str = dt.strftime("%B %d, %Y")
dt = datetime.datetime.strptime(dt_str, "%B %d, %Y")
print(dt)
