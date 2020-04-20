class boyermoore :
    def __init__ (self) :
        pass

    def lastOccuranceFunction (self, pattern) :
        lastOccurance = [-1]*256
        for i in range (len(pattern)) :
            lastOccurance[ord(pattern[i])] = i
        return lastOccurance

    def match(self, text, pattern) :
        m = len(pattern)
        n = len(text)
        i = m - 1
        lastOccurance = self.lastOccuranceFunction(pattern)

        if (i > (n - 1)) :
            return -1

        j = m - 1
        while (i <= (n - 1)):
            if (text[i] == pattern[j]) :
                if (j == 0) :
                    return i
                else :
                    i -= 1
                    j -= 1
            else :
                lo = lastOccurance[ord(text[i])]
                i = i + m - min(j, lo + 1)
                j = m - 1
        
        return -1
