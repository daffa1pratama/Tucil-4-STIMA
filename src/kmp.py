class kmp :
    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text

    def failureFunction(self) :
        failure = [0] * len(self.pattern)
        m = len(self.pattern)
        i = 1
        j = 0

        while (i < m) :
            if (self.pattern[i] == self.pattern[j]) :
                failure[i] = j + 1
                i += 1
                j += 1
            elif (j > 0) :
                j = failure[j-1]
            else :
                failure[i] = 0
                i += 1
        return failure

    def matchKMP(self) :
        m = len(self.pattern)
        n = len(self.text)
        i = 0
        j = 0
        failure = self.failureFunction()

        while (i < n) :
            if (self.text[i] == self.pattern[j]) :
                if (j == (m - 1)) :
                    return i - m + 1
                i += 1
                j += 1
            elif (j > 0) :
                j = failure[j-1]
            else :
                i += 1
        
        return -1