class kmp :
    def __init__(self):
        pass

    def failureFunction(self, pattern) :
        failure = [0] * len(pattern)
        m = len(pattern)
        i = 1
        j = 0

        while (i < m) :
            if (pattern[i] == pattern[j]) :
                failure[i] = j + 1
                i += 1
                j += 1
            elif (j > 0) :
                j = failure[j-1]
            else :
                failure[i] = 0
                i += 1
        return failure

    def match(self, text, pattern) :
        m = len(pattern)
        n = len(text)
        i = 0
        j = 0
        failure = self.failureFunction(pattern)

        while (i < n) :
            if (text[i] == pattern[j]) :
                if (j == (m - 1)) :
                    return i - m + 1
                i += 1
                j += 1
            elif (j > 0) :
                j = failure[j-1]
            else :
                i += 1
        
        return -1