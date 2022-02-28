nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n' for each 'n' in nums
# my_list = [n * n for n in nums]
# print(my_list)

# my_list = list(map(lambda n: n * n, nums))
# print(my_list)

# my_list = [n for n in nums if n % 2 == 0]
# print(my_list)

# my_list = list(filter(lambda n: n % 2 == 0, nums))
# print(my_list)

# my_list = [(letter, num) for letter in "abcd" for num in range(4)]
# print(my_list)

# Dictionary Comprehensions
names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]

my_dict = {name: hero for name, hero in zip(names, heros) if name != "Peter"}
print(my_dict)
