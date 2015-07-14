class File:
    def __init__(self, filename):
        self.filename = filename

    def getSize(self):
        my_file = open("test.file", "rb")

        byte_count = 0
        while my_file.read(1):
            byte_count += 1
        my_file.close()

class FileSplitter:
    def __init__(self, file):
        self.file = file
