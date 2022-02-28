from datetime import datetime

first_name = "Musleh"
last_name = "Khan"

person = {"name": "Musleh", "age": 22}

# sentence = f"My name is {person['name']} and I am {person['age']} years old"
# sentence = "My name is {name} and I am {age} years old".format(**person)

birthday = datetime(1999, 3, 10)

sentence = f"Musleh has a birthday on {birthday:%B %d, %Y}"

print(sentence)
