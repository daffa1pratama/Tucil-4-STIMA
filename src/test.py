from textReader import *
from nltk import tokenize
import re

sentenceContainer = []
f = textReader("../test/jabar11042020.txt").readText()
# query = '([1-9]|1[0-9]|2[0-9]|3[0-1])(\/|-)([1-9]|1[0-2])(\/|-|)(20[0-9][0-9])'
# hasil = re.compile(query, re.M)
for i in range(len(f)) :
    temp = tokenize.sent_tokenize(f[i])
    for i in range(len(temp)) :
        sentenceContainer.append(temp[i])
    # print(tokenize.sent_tokenize(f[i]))
print(sentenceContainer)
#     print("INI F[i]")
#     print(f[i])
#     print("INI HASIL")
#     print(hasil.findall(f[i]))

# print(f)
# print(hasil)

# pat = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)
# print(pat.findall('OMG is this a question ! Is this a sentence ? My. name is.'))

# DATE : 
# dd-mm-yyyy or dd/mm/yyyy = ([1-9]|1[0-9]|2[0-9]|3[0-1])(\/|-)([1-9]|1[0-2])(\/|-|)(20[0-9][0-9])
# dd nama yyyy = ([1-9]|1[0-9]|2[0-9]|3[0-1]) (Jan(?:uari)?|Feb(?:uary)?|Mar(?:et)?|Apr(?:il)?|Mei|Jun(?:i)?|Jul(?:i)?|Agu(?:stus)?|Ags|Sep(?:tember)?|Okt(?:ober)?|Nov(?:ember)?|Des(?:ember)?) (20[0-9][0-9])

# DAY : 

# TIME :
# hh:mm = ^(([01]\d|2[0-3]):([0-5]\d)|24:00)$
# NUMBERS : [0-9]*[.,]{0,1}[0-9]*