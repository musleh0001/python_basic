import math
import statistics
from functools import reduce

def area(r):
   """ Area of circle with radius 'r'. """
   return math.pi * (r**2)

radii = [2, 5, 7.1, 0.3, 10]

# Method 01: Direct Method
areas = []
for r in radii:
    a = area(r)
    areas.append(a)

print("\nMap")
print(areas)

# Method 02: Use 'map' function
# map(function, data) return iterator
print("\nMap")
print(list(map(area, radii)))

# Example
temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 29), ("Los Angeles", 26), ("Tokyo", 27), ("New York", 28), ("London", 22), ("Beijing", 22)]

c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)

print("\nMap")
print(list(map(c_to_f, temps)))

# Filter
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print("\nFilter")
print(list(filter(lambda x: x > avg, data)))


# Remove missing data
print("\nFilter")
countries = ["", "Argentina", "", "Brazil", "Chile", "", "Colombia", "", "Ecuador", "", "", "Venezuela"]
print(list(filter(None, countries)))


# Reduce Function
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print("\nReduce")
print(reduce(lambda x, y: x*y, data))
