class boyermoore :
    def __init__ (self, pattern, text) :
        self.text = text
        self.pattern = pattern
        self.lastOccurance = [-1]*256

    def lastOccuranceFunction (self) :
        for i in range (len(self.pattern)) :
            self.lastOccurance[ord(self.pattern[i])] = i
        return self.lastOccurance

    def matchBoyerMoore (self) :
        m = len(self.pattern)
        n = len(self.text)
        i = m - 1

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
                lo = self.lastOccurance[ord(self.text[i])]
                i = i + m - min(j, lo + 1)
                j = m - 1
        
        return -1
