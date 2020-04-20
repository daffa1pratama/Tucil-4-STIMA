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
pattern = "positif"
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
for text in sentenceContainer :
    # if (alg.match(text, pattern) != -1) :
    # temp = re.findall(queryDay, text)
    # print(temp)
    # for res in temp :
        # print(res)
        # text = text.replace(res, '<span style="color:blue">'+res+'</span>')
        # text.replace(res, '<b>'+res+'<b>')
    # text = text.replace(pattern, '<b>'+pattern+'</b>')
    subsSentence = []
    text = text.split(' ')
    for sub in text :
        subsSentence.append(sub)
    newContainer.append(subsSentence)
    # print(subsSentence, end='<br>')
    # print(text, end='<br>')

# print(newContainer, end='<br>')
for row in newContainer :
    # print(row, end='<br>')
    i = 0
    temp = []
    while i < (len(row)) :
        if (re.match(queryNumber, row[i])) :
            # Case date
            if (re.match(queryMonth, row[i+1]) and re.match(queryNumber, row[i+2])) :
                temp.append(row[i] + ' ' + row[i+1] + ' ' + row[i+2])
                i += 2
            # Case time
            elif (re.match(queryTime, row[i+1])) :
                temp.append(row[i] + ' ' + row[i+1])
            # Case number
            else :
                number.append(row[i])
        # Case day
        elif (re.match(queryDay, row[i])) :
            temp.append(row[i])
        # Case date
        elif (re.match(queryDate, row[i])) :
            print("ini brow")
            print(row[i])
            temp.append(row[i])

        i = i + 1
    date.append(temp)
        # print(row[i], end='<br>')
        # temp = re.findall(queryNumber, row)
        # for res in temp :
        #     number.append(res)

print(number)
print(date)