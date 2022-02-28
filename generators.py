import memory_profiler as mem_profile
import random
import time


# def square_numbers(nums):
#     for i in nums:
#         yield (i * i)


# my_nums = square_numbers(list(range(1, 6)))

# my_nums = (x * x for x in range(1, 6))
# print(my_nums)

# for num in my_nums:
#     print(num)


names = ["John", "Corey", "Adam", "Steve", "Rick", "Thomas"]
majors = ["Math", "Engineering", "CompSci", "Arts", "Business"]

print(f"Memory (Before): {mem_profile.memory_usage()}Mb")


def people_list(num_people):
    result = []

    for i in range(num_people):
        person = {"id": i, "name": random.choice(names), "major": random.choice(majors)}
        result.append(person)
    return result


# memory efficient
def people_generator(num_people):
    for i in range(num_people):
        person = {"id": i, "name": random.choice(names), "major": random.choice(majors)}
        yield person


start = time.perf_counter()
people = people_generator(1000000)
end = time.perf_counter()

print(f"Memory (After): {mem_profile.memory_usage()}Mb")
print(f"Took {end - start:.4f} seconds")
