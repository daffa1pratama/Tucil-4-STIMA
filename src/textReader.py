class textReader :
    def __init__(self, filepath) :
        self.filepath = filepath
        self.stream = []

    def readText(self) :
        f = open(self.filepath, 'r')
        temp = f.readlines()
        for i in range(len(temp)) :
            self.stream.append(temp[i].strip("\n"))
        return self.stream