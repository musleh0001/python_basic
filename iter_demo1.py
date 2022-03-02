import itertools

letters = ['a', 'b', 'c', 'd']
numbers = list(range(0, 4))
names = ['Musleh', 'Khan']

# result = itertools.combinations(letters, 2)
# result = itertools.permutations(letters, 2) 
# for item in result:
#     print(item)

combined = itertools.chain(letters, numbers, names)
for item in combined:
    print(item)


# counter = itertools.count(start=5, step=5)
# print(next(counter))
# print(next(counter))
# print(next(counter))

# data = [100, 200, 300, 400]
# daily_data = list(zip(itertools.count(), data))
# daily_data = list(itertools.zip_longest(range(10), data))
# print(daily_data)

# counter = itertools.cycle(('On', 'Off'))
# counter = itertools.repeat(2, times=3)

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# Example
# squares = map(pow, range(10), itertools.repeat(2))
# squares = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])
# print(list(squares))
