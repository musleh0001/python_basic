import random

# value = random.random()
# value = random.uniform(1, 10)
# value = random.randint(1, 10)

# greeting = ["Hello", "Hi", "Hey", "Howdy", "Hola"]
# value = random.choice(greeting)

# colors = ["Red", "Black", "Green"]
# value = random.choices(colors, weights=[18, 18, 2], k=10)

value = list(range(1, 53))
random.shuffle(value)
# hand = random.sample(value, k=5)


print(value)
