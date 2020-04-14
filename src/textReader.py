class textReader :
    def __init__(self, filepath) :
        self.filepath = filepath
        self.stream = []

    def readText(self) :
        f = open(self.filepath, 'r')
        self.stream = f.readlines()
        return self.stream