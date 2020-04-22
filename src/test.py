# from textReader import *
# from nltk import tokenize
import re

# sentenceContainer = []
# keywordContainer = []
# f = textReader("../test/jabar11042020.txt").readText()
# query = r'([0-9]+[.,]?[0-9]*)'
# # hasil = re.compile(query)
# for i in range(len(f)) :
#     temp = tokenize.sent_tokenize(f[i])
#     for i in range(len(temp)) :
#         sentenceContainer.append(temp[i])

# print(sentenceContainer)

# for i in range(len(sentenceContainer)) :
#     print("INI KALIMAT KE[i]")
#     print(sentenceContainer[i])
#     print("INI HASIL")
#     temp = re.findall(query, sentenceContainer[i])
#     print(temp)
#     # if (len(temp) != 0) :
#         # keywordContainer.append(max(temp[0], key=len))
#         # for j in range (len(temp)) :
#         #     keywordContainer.append(temp[j])

# print(keywordContainer)

# # print(f)
# # print(hasil)

# # DATE : 
# # dd-mm-yyyy or dd/mm/yyyy = (([1-9]|1[0-9]|2[0-9]|3[0-1])(\/|-)([1-9]|1[0-2])(\/|-|)([0-9]{0,4}))
# # dd nama yyyy = (([1-9]|1[0-9]|2[0-9]|3[0-1]) (Jan(?:uari)?|Feb(?:uary)?|Mar(?:et)?|Apr(?:il)?|Mei|Jun(?:i)?|Jul(?:i)?|Agu(?:stus)?|Ags|Sep(?:tember)?|Okt(?:ober)?|Nov(?:ember)?|Des(?:ember)?) ([0-9]{0,4}))

# # DAY : ()

# # TIME :
# # hh:mm = ^(([01]\d|2[0-3]):([0-5]\d)|24:00)$
# # NUMBERS : ([0-9]+[.,]?[0-9]*)

# queryTime = "(([01]\d|2[0-3]):([0-5]\d)|24:00)"
# queryTime = "((([0]?[1-9]|1[0-9]|2[0-4])(:|\.)[0-5][0-9]((:|\.)[0-5][0-9])?( )?(wib|wita|wit))|(([0]?[0-9]|1[0-9]|2[0-3])(:|\.)[0-5][0-9]((:|\.)[0-5][0-9])?))"
# queryDate = "(([1-9]|1[0-9]|2[0-9]|3[0-1]) (jan(?:uari)?|feb(?:uary)?|mar(?:et)?|apr(?:il)?|mei|jun(?:i)?|jul(?:i)?|agu(?:stus)?|ags|sep(?:tember)?|okt(?:ober)?|nov(?:ember)?|des(?:ember)?) ([0-9]{0,4}))"

# queryMonth = "(jan(?:uari)?|feb(?:ruari)?|mar(?:et)?|apr(?:il)?|mei|jun(?:i)?|jul(?:i)?|agu(?:stus)|ags|sep(?:tember)?|okt(?:ober)?|nov(?:ember)?|des(?:ember)?)"
queryMonth = r"\b(januari|februari|maret|april|mei|juni|juli|agustus|september|oktober|november|desember|jan|feb|mar|apr|jun|jul|ags|agu|sep|okt|nov|des)\b"
# queryMonth = "\bjanuari|jan"
# if (re.search(queryMonth, '11 jan')) :
#     print("HOP")
# if (re.match(queryMonth, '11 jan')) :
#     print("WES")
text = 'apri-12'
print(re.match(queryMonth, text))
print(re.findall(queryMonth, text))