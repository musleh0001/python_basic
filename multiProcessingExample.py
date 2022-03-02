import concurrent.futures
import time
from PIL import Image, ImageFilter


img_names = [
    "photo-1516117172878-fd2c41f4a759.jpg",
    "photo-1532009324734-20a7a5813719.jpg",
    "photo-1522364723953-452d3431c267.jpg",
    "photo-1513938709626-033611b8cc03.jpg",
    "photo-1507143550189-fed454f93097.jpg",
    "photo-1530122037265-a5f1f91d3b99.jpg",
    "photo-1516972810927-80185027ca84.jpg",
    "photo-1550439062-609e1531270e.jpg",
]

t1 = time.perf_counter()

size = (1200, 1200)


def process_image(img_name):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f"processed/{img_name}")
    print(f"{img_name} was processed...")


# with concurrent.futures.ProcessPoolExecutor() as executor:
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(process_image, img_names)

t2 = time.perf_counter()

print(f"Finished in {t2-t1} seconds")
