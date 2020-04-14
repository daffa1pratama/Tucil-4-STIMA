from textReader import *
from kmp import *
from boyermoore import *
from regex import *
import sys

# class main :
#     def __init__(self, pattern, filename, algoritma) :
#         self.pattern = pattern
#         self.filename = filename
#         self.algoritma = algoritma
    # text = textReader('../test/jabar11042020.txt').readText()
    # print(text)
text = "abacaabaccabacabaabb"
pattern = "abacab"
algoritma = sys.argv[1]
    # kmp = kmp(pattern, text)
    # failure = kmp.failureFunction()
    # print(failure)
    # match = kmp.matchKMP()
    # print(match)

    # bm = boyermoore(pattern, text)
    # last = bm.lastOccuranceFunction()
    # print(last)
    # matchx = bm.matchBoyerMoore()
    # print(matchx)

    # reg = regex(pattern, text)
    # matchr = reg.matchRegex()
    # print(matchr)


if (algoritma == "boyermoore") :
    bm = boyermoore(pattern, text)
    last = bm.lastOccuranceFunction() 
    matchx = bm.matchBoyerMoore()
    print(matchx)
else :
    print("BLOM ADA")

# if __name__ == '__main__':
#     main("abacab", "abacaabaccabacabaabb", sys.argv[1])
#     # main()
#     print(sys.argv[1])
    