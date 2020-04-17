import re

class ruegex :
    def __init__(self, pattern, text) :
        self.pattern = pattern
        self.text = text

    def matchRegex(self) :
        x = re.search(self.pattern, self.text)
        if (x != none) :
            return x.start()
        return -1