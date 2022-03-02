# nums = list(range(1, 9))

# i_nums = iter(nums)

# while True:
#     try:
#         item = next(i_nums)
#         print(item)
#     except StopIteration:
#         break

class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

nums = MyRange(1, 10)

# for num in nums:
    # print(num)

# print(next(nums))

