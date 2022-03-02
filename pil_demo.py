from PIL import Image, ImageFilter
import os

# size_300 = (300, 300)

# for f in os.listdir("/home/musleh/Pictures/"):
#     if f.endswith(".jpg"):
#         # print(f)
#         i = Image.open(f"/home/musleh/Pictures/{f}")
#         fn, text = os.path.splitext(f)
#         i.thumbnail(size_300)
#         i.save(
#             f"/home/musleh/programming/language/python/basic_new/pngs/{fn}_300{text}"
#         )

image1 = Image.open("./pngs/leahGotti.jpg")
# image1.rotate(90).save("./pngs/leahGotti_rotated.jpg")
# image1.convert("L").save("./pngs/leahGotti_converted.jpg")  # grayscale
image1.filter(ImageFilter.GaussianBlur(15)).save("./pngs/leahGotti_blurred.jpg")
