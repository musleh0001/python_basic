import datetime
import pytz

a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
b = str(a)

print(f"{str(a) = }")
print(f"{str(b) = }")

print()

print(f"{repr(a) = }")
print(f"{repr(b) = }")
