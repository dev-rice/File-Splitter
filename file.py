class File:
    def __init__(self, filename):
        self.filename = filename

    def getSize(self):
        my_file = open("test.file", "rb")

        byte_count = 0
        while my_file.read(1):
            byte_count += 1
        my_file.close()

        return byte_count

    def setBytes(self, bytes):
        # Take an array of bytes and write them to the file

        pass

    def getBytes(self):
        # Read the file and return an array of bytes, maybe should cache this

    def appendBytes(self, bytes):
        # Take an array of bytes and add them to the
        # end of the file
        pass
