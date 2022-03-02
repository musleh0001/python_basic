def find_index(to_search, target):
    for index, value in enumerate(to_search):
        if value == target:
            break
    else:
        return -1
    return index


my_list = ["musleh", "mahmudul", "imran"]
index_location = find_index(my_list, "imran")

print(f"Location of target is index: {index_location}")
