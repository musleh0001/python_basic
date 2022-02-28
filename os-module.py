import os
from datetime import datetime

print(dir(os))

# get current dir
print(os.getcwd())
os.chdir("/home/musleh/Desktop")
print(os.getcwd())

# list dir
print(os.listdir())
print(os.listdir("/home/musleh/programming"))

# can't make subdir
os.mkdir("OS-Demo-2")
# can make subdir
os.makedirs("OS-Demo-2/Sub-Dir-1")

# delete dir
os.rmdir("OS-Demo-2")
os.removedirs("OS-Demo-2/Sub-Dir-1")

# rename dir
os.rename("test.txt", "demo.txt")

# read file content
print(os.stat("demo.txt"))

mod_time = os.stat("os-module.py").st_mtime
print(datetime.fromtimestamp(mod_time))

# entir dir tree
# #%%
for dirpath, dirnames, filenames in os.walk("/home/musleh/Pictures"):
    print(f"Current Path: {dirpath}")
    print(f"Directories: {dirnames}")
    print(f"Filesw: {filenames}")
    print()

# get environ variable
print(os.environ.get("HOME"))

file_path = os.path.join(os.environ.get("HOME"), "test.txt")
print(file_path)

#%%
print(os.path.basename("/tmp/text.txt"))
print(os.path.dirname("/tmp/text.txt"))
print(os.path.split("/tmp/text.txt"))
print(os.path.exists("/tmp/text.txt"))

# %%
print(os.path.isdir("/tmp/somename"))
print(os.path.isfile("/tmp/somename"))
print(os.path.splitext("/tmp/test.txt"))

# %%
