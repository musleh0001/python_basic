# Tips 01
print("Tips 01")
condition = True
x = 1 if condition else 0
print(x)


# Tips 02
print("\nTips 02")
num1 = 10_000_000_000
num2 = 100_000_000
total = num1 + num2
print(f"{total:,}")


# Tips 03
print("\nTips 03")
with open("test.txt", "r") as f:
    file_contents = f.read()

words = file_contents.split(" ")
print(len(words))


# Tips 04
print("\nTips 04")
names = ["musleh", "imran", "mahmudul", "John"]
for index, name in enumerate(names, start=1):
    print(index, name)


# Tips 05
print("\nTips 05")
names = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
heros = ["Spiderman", "Superman", "Deadpool", "Batman"]
universes = ["Marvel", "DC", "Marvel", "DC"] 

for name, hero, universe in zip(names, heros, universes):
    print(f"{name} is actually {hero} from {universe}")


# Tips 06
print("\nTips 06")
a, _ = (1, 2)
a, b, *c = (1, 2, 3, 4, 5, 6, 7)
a, b, *_ = (1, 2, 3, 4, 5, 6, 7)
a, *_, c = (1, 2, 3, 4, 5, 6, 7)


# Tips 07
print("\nTips 07")
from getpass import getpass

username = input("Username: ")
password = getpass("Password: ")
print("Logging In...")
