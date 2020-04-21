# from textReader import *
# from nltk import tokenize
# import re

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

a = [1,2,3,4]
b = a.copy()
b.pop(0)
print(a)
print(b)