# File objects

# normal
# f = open("test.txt", "r")
# print(f.name, f.mode)
# f.close()

# context manager
# with open("test.txt", "r") as f:
#     # size_to_read = 100
#     # f_contents = f.read(size_to_read) # print 1st 100 char
#     # f_contents = f.readline()  # print one line
#     # f_contents = f.readlines()
#     # print(f_contents)

#     # to access large file
#     # for line in f:
#     #     print(line, end="")

#     # another approch
#     size_to_read = 100
#     f_contents = f.read(size_to_read)
#     print(f.tell())  # tell current file pointer
#     f.seek(0)  # set file pointer to 0
#     while len(f_contents) > 0:
#         print(f_contents, end="")
#         f_contents = f.read(size_to_read)


with open("test.txt", "rb") as rf:
    with open("test_copy.txt", "wb") as wf:
        # for line in rf:
        # wf.write(line)
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
