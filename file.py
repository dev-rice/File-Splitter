class File:
    def __init__(self, filename):
        self.filename = filename

    def getSize(self):
        my_file = open(self.filename, "rb")

        byte_count = 0
        while my_file.read(1):
            byte_count += 1
        my_file.close()

        return byte_count

    def setBytes(self, bytes):
        # Take an array of bytes and write them to the file
        my_file = open(self.filename, "wb")

        my_file.write(bytes)

    def getBytes(self, num_bytes = None, starting_byte = 0):
        # Read the file and return an array of bytes, maybe should cache this
        if (num_bytes == None):
            num_bytes = self.getSize()

        my_file = open(self.filename, "rb")

        my_file.seek(starting_byte)
        all_bytes = my_file.read(num_bytes)

        print("tell = " + str(my_file.tell()))

        return all_bytes


    def appendBytes(self, bytes):
        # Take an array of bytes and add them to the
        # end of the file
        pass
