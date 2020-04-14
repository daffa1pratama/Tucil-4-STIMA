class kmp :
    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text
        self.failure = [0] * len(self.pattern)

    def failureFunction(self) :
        self.failure[0] = 0
        m = len(self.pattern)
        i = 1
        j = 0

        while (i < m) :
            if (self.pattern[i] == self.pattern[j]) :
                self.failure[i] = j + 1
                i += 1
                j += 1
            elif (j > 0) :
                j = self.failure[j-1]
            else :
                self.failure[i] = 0
                i += 1
        return self.failure

    def matchKMP(self) :
        m = len(self.pattern)
        n = len(self.text)
        i = 0
        j = 0

        while (i < n) :
            if (self.text[i] == self.pattern[j]) :
                if (j == (m - 1)) :
                    return i - m + 1
                i += 1
                j += 1
            elif (j > 0) :
                j = self.failure[j-1]
            else :
                i += 1
        
        return -1