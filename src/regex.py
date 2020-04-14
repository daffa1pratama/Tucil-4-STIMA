import re

class regex :
    def __init__(self, pattern, text) :
        self.pattern = pattern
        self.text = text

    def matchRegex(self) :
        x = re.search(self.pattern, self.text)
        return x.start()