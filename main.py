my_file = open("test.file", "rb")

byte_count = 0
while my_file.read(1):
    byte_count += 1

print(byte_count)
