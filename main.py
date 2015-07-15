from file import *
import math

my_file = File("test.file")
file_size = my_file.getSize()

file1_percent = 0.3
file2_percent = 0.7

file1_size = math.ceil(file1_percent * file_size)
file2_size = math.floor(file2_percent * file_size)

file_size_test = file1_size + file2_size
if (file_size_test == file_size):
    print("is ok")

file1_bytes = my_file.getBytes(file1_size, 0)
file2_bytes = my_file.getBytes(file2_size, file1_size)

file1 = File("test.file.part1")
file1.setBytes(file1_bytes)

file2 = File("test.file.part2")
file2.setBytes(file2_bytes)



print(file_size)
