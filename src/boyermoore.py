class boyermoore :
    def __init__ (self, pattern, text) :
        self.text = text
        self.pattern = pattern

    def lastOccuranceFunction (self) :
        lastOccurance = [-1]*256
        for i in range (len(self.pattern)) :
            lastOccurance[ord(self.pattern[i])] = i
        return lastOccurance

    def matchBoyerMoore (self) :
        m = len(self.pattern)
        n = len(self.text)
        i = m - 1
        lastOccurance = self.lastOccuranceFunction()

        if (i > (n - 1)) :
            return -1

        j = m - 1
        while (i <= (n - 1)):
            if (self.text[i] == self.pattern[j]) :
                if (j == 0) :
                    return i
                else :
                    i -= 1
                    j -= 1
            else :
                lo = lastOccurance[ord(self.text[i])]
                i = i + m - min(j, lo + 1)
                j = m - 1
        
        return -1
