from textReader import *
from kmp import *
from boyermoore import *
from reg import *
from nltk import tokenize
import sys

def searchIndex(pattern, text) :
    pat = pattern.split(' ')
    for i in range(len(text)) :
        same = False
        if (pat[0] == text[i]) :
            j = 1
            while (j < len(pat)) :
                if (pat[j] != text[i+j]) :
                    return -1
                j += 1
            same = True
        if (same) :
            return i
    return -1

# Init
filename = sys.argv[1]
pattern = sys.argv[2]
algoritma = sys.argv[3]
# filename = "jabar11042020.txt"
# pattern = "terkonfirmasi positif"
# algoritma = "kmp"
sentenceContainer = []
newContainer = []
date = []
number = []

# Load text
f = textReader("uploaded/" + filename).readText()
for row in f :
    temp = tokenize.sent_tokenize(row)
    for text in temp :
        sentenceContainer.append(text.lower())

# Select algorithm
if (algoritma == "boyermoore") :
    alg = boyermoore()
elif (algoritma == "kmp") :
    alg = kmp()
else :
    alg = reg()

queryNumber = "^([0-9]+([\.,:]?[0-9]*)*)$"
queryDate = ".?(([1-9]|1[0-9]|2[0-9]|3[0-1])(/|-)(0?[1-9]|1[0-2])(/|-|)([0-9]{0,4})).?"
# queryMonth = "^(jan(?:uari)?|feb(?:uary)?|mar(?:et)?|apr(?:il)?|mei|jun(?:i)?|jul(?:i)?|agu(?:stus)?|ags|sep(?:tember)?|okt(?:ober)?|nov(?:ember)?|des(?:ember)?)"
queryMonth = "^(januari|februari|maret|april|mei|juni|juli|agustus|september|oktober|november|desember|jan|feb|mar|apr|jun|jul|ags|sep|okt|nov|des)"
queryDay = "\b(senin|selasa|rabu|kamis|jumat|sabtu|minggu)\b"
queryTime = "^(wib|wita|wit)"

# Sub sentence
for row in sentenceContainer :
    subsSentence = []
    row = row.split(' ')
    for sub in row :
        subsSentence.append(sub)
    newContainer.append(subsSentence)

# Extraction + Print text
print("Filename : " + filename, end='<br>')
print("===============================================", end='<br>')
for row in newContainer :
    i = 0
    dateTemp = []
    numberTemp = []
    res = ''
    while i < (len(row)) :
        if (re.match(queryNumber, row[i])) :
            # Case date
            if (re.match(queryMonth, row[i+1])) :
                # Case month
                if (re.match(queryNumber, row[i+2])) :
                    dateTemp.append(row[i] + ' ' + row[i+1] + ' ' + row[i+2])
                    res += '<span style="color: red">' + row[i] + ' ' + row[i+1] + ' ' + row[i+2] + '</span>' + ' '
                    i += 2
                # Case without month
                else :
                    dateTemp.append(row[i] + ' ' + row[i+1])
                    res += '<span style="color: red">' + row[i] + ' ' + row[i+1] + '</span>' + ' '
                    i += 1
            # Case time
            elif (re.match(queryTime, row[i+1])) :
                dateTemp.append(row[i] + ' ' + row[i+1])
                res += '<span style="color: red">' + row[i] + ' ' + row[i+1] + '</span>' + ' '
                i += 1
            # Case number
            else :
                numberTemp.append(row[i])
                res += '<span style="color: blue">' + row[i] + '</span>' + ' '
        # Case month only
        elif (re.match(queryMonth, row[i])) :
            print("INI C: " + row[i], end="<br>")
            dateTemp.append(row[i])
            res += '<span style="color: red">' + row[i] + '</span>' + ' '
        # Case day
        elif (re.match(queryDay, row[i])) :
            dateTemp.append(row[i])
            res += '<span style="color: red">' + row[i] + '</span>' + ' '
        # Case date
        elif (re.match(queryDate, row[i])) :
            dateTemp.append(row[i])
            res += '<span style="color: red">' + row[i] + '</span>' + ' '
        # Another
        else :
            res += row[i] + ' '
        i = i + 1
    date.append(dateTemp)
    number.append(numberTemp)
    print(res, end='<br>')
print("===============================================", end='<br>')

# Construct date
for i in range(len(date)) :
    temp = ''
    dateSize = len(date[i])
    for j in range(dateSize) :
        temp += date[i].pop(0)
        if (j != dateSize-1) :
            temp += ' '
    date[i] = temp

# Get news date
for row in date :
    if (len(row) != 0) :
        newsDate = row
        break

# Nearest number
# for i in range(len(newContainer)) :
#     patternIdx = searchIndex(pattern, newContainer[i])
#     # print("PATTERN IDX : ", end="")
#     # print(patternIdx)
#     numberIdx = []
#     # dateIdx = []
#     tempNum = number[i].copy()
#     # tempDate = date[i].copy()
#     for word in newContainer[i] :
#         if (word in tempNum) :
#             num = tempNum.pop(0)
#             # print(num)
#             numberIdx.append(abs(searchIndex(num, newContainer[i]) - patternIdx))
#         # if (word in)
#     # print("NUMBER IDX : ", end="")
#     # print(numberIdx)
#     if (len(numberIdx) != 0) :
#         nearest = min(numberIdx)
#         index = numberIdx.index(nearest)
        # print(index)
    # if (len(number[i]) != 0) :
        # print(number[i][index])
    # print("===================")

# Result + Print Result
print("Keyword\t: " + pattern, end='<br>')
print("Hasil ekstraksi informasi\t:", end='<br>')
for i in range (len(sentenceContainer)) :
    if (alg.match(sentenceContainer[i], pattern) != -1) :
        patternIdx = searchIndex(pattern, newContainer[i])
        numberIdx = []
        tempNum = number[i].copy()
        for word in newContainer[i] :
            if (word in tempNum) :
                num = tempNum.pop(0)
                numberIdx.append(abs(searchIndex(num, newContainer[i]) - patternIdx))
        if (len(numberIdx) != 0) :
            nearest = min(numberIdx)
            index = numberIdx.index(nearest)
        print("Jumlah\t: ")
        if (len(number[i]) != 0) :
            print(number[i][index], end='<br>')
        else :
            print("-", end='<br>')
        print("Tanggal\t: ")
        if (len(date[i]) != 0) :
            print(date[i], end='<br>')
        else :
            print(newsDate, end='<br>')
        print(sentenceContainer[i], end='<br>')
        print("===================", end='<br>')

print(date)