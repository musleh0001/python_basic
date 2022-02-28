from collections import namedtuple

# list / tuple
color = (55, 155, 255)

# dictionary
color = {"red": 55, "green": 155, "blue": 255}

# named tuple
Color = namedtuple("Color", ["red", "green", "blue"])
# color = Color(red=55, green=155, blue=255)
color = Color(55, 155, 255)

print(color[0])
print(color.red)
