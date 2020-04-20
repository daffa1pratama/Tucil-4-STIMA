from textReader import *
from kmp import *
from boyermoore import *
from reg import *
from nltk import tokenize
import sys

# Init
# filename = sys.argv[1]
# pattern = sys.argv[2]
# algoritma = sys.argv[3]
filename = "jabar11042020.txt"
pattern = "covid"
algoritma = "boyermoore"
sentenceContainer = []
date = []
number = []
newContainer = []

# Load text
f = textReader("uploaded/" + filename).readText()
for row in f :
    temp = tokenize.sent_tokenize(row)
    for text in temp :
        sentenceContainer.append(text.lower())

# Print text
print("============================")
for i in range(len(sentenceContainer)) :
    print(sentenceContainer[i])
print("============================")

# Select algorithm
if (algoritma == "boyermoore") :
    alg = boyermoore()
elif (algoritma == "kmp") :
    alg = kmp()
else :
    alg = reg()

queryNumber = "^([0-9]+[.,:]?[0-9]*)$"
# queryDate = "(([1-9]|1[0-9]|2[0-9]|3[0-1]) (jan(?:uari)?|feb(?:uary)?|mar(?:et)?|apr(?:il)?|mei|jun(?:i)?|jul(?:i)?|agu(?:stus)?|ags|sep(?:tember)?|okt(?:ober)?|nov(?:ember)?|des(?:ember)?) ([0-9]{0,4}))"
queryDate = ".?(([1-9]|1[0-9]|2[0-9]|3[0-1])(/|-)(0?[1-9]|1[0-2])(/|-|)([0-9]{0,4})).?"
queryMonth = "^(jan(?:uari)?|feb(?:uary)?|mar(?:et)?|apr(?:il)?|mei|jun(?:i)?|jul(?:i)?|agu(?:stus)?|ags|sep(?:tember)?|okt(?:ober)?|nov(?:ember)?|des(?:ember)?)"
queryDay = "(senin|selasa|rabu|kamis|jumat|sabtu|minggu)"
# queryTime = "(([01]\d|2[0-3]):([0-5]\d)|24:00)"
# queryTime = "((([0]?[1-9]|1[0-9]|2[0-4])(:|\.)[0-5][0-9]((:|\.)[0-5][0-9])?( )?(wib|wita|wit))|(([0]?[0-9]|1[0-9]|2[0-3])(:|\.)[0-5][0-9]((:|\.)[0-5][0-9])?))"
queryTime = "^(wib|wita|wit)"

# Print result (bold)
for row in sentenceContainer :
    # if (alg.match(text, pattern) != -1) :
    # temp = re.findall(queryDay, text)
    # print(temp)
    # for res in temp :
        # print(res)
        # text = text.replace(res, '<span style="color:blue">'+res+'</span>')
        # text.replace(res, '<b>'+res+'<b>')
    # text = text.replace(pattern, '<b>'+pattern+'</b>')
    subsSentence = []
    row = row.split(' ')
    for sub in row :
        subsSentence.append(sub)
    newContainer.append(subsSentence)
    # print(subsSentence, end='<br>')
    # print(text, end='<br>')

for row in newContainer :
    i = 0
    dateTemp = []
    numberTemp = []
    while i < (len(row)) :
        if (re.match(queryNumber, row[i])) :
            # Case date
            if (re.match(queryMonth, row[i+1]) and re.match(queryNumber, row[i+2])) :
                dateTemp.append(row[i] + ' ' + row[i+1] + ' ' + row[i+2])
                i += 2
            # Case time
            elif (re.match(queryTime, row[i+1])) :
                dateTemp.append(row[i] + ' ' + row[i+1])
            # Case number
            else :
                numberTemp.append(row[i])
        # Case day
        elif (re.match(queryDay, row[i])) :
            dateTemp.append(row[i])
        # Case date
        elif (re.match(queryDate, row[i])) :
            dateTemp.append(row[i])

        i = i + 1
    date.append(dateTemp)
    number.append(numberTemp)

# Get news date
for row in date :
    if (len(row) != 0) :
        newsDate = row
        break

# RESULT
for i in range (len(sentenceContainer)) :
    if (alg.match(sentenceContainer[i], pattern) != -1) :
        print("TEKS : ", end="")
        print(sentenceContainer[i])
        print("TANGGAL : ", end="")
        if (len(date[i]) != 0) :
            print(date[i])
        else :
            print(newsDate)
        print("JUMLAH : ", end="")
        if (len(number[i]) != 0) :
            print(number[i])
        else :
            print("-")
        print("===================")
# print(number)
# print(date)