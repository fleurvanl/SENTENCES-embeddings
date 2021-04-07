# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 13:22:24 2021

@author: aluenen
"""
#prep data
import os
import json
import spacy
nlp = spacy.load('nl_core_news_sm')
#from nltk import sent_tokenize
from preprocessing import Preprocessing
prepro = Preprocessing()

os.chdir('D:/Newsdata')
print("Current Working Directory " , os.getcwd())

f = open('trouw (print).json', 'r')
print('file opened')

with open('trouwtokenized2010.json', 'w') as writefile:
    writefile.write("[")
    
with open('trouwtokenized2011.json', 'w') as writefile:
    writefile.write("[")
    
with open('trouwtokenized2012.json', 'w') as writefile:
    writefile.write("[")
    
with open('trouwtokenized2013.json', 'w') as writefile:
    writefile.write("[")
    
with open('trouwtokenized2014.json', 'w') as writefile:
    writefile.write("[")
    
with open('trouwtokenized2015.json', 'w') as writefile:
    writefile.write("[")
    
with open('trouwtokenized2016.json', 'w') as writefile:
    writefile.write("[")
    
with open('trouwtokenized2017.json', 'w') as writefile:
    writefile.write("[")
    
with open('trouwtokenized2018.json', 'w') as writefile:
    writefile.write("[")

nnotext = 0
anytext = 0
counter = 0

#create class

for line in f:
    counter += 1
    article = json.loads(line)
    date = article["publication_date"]
    year = int(date[:4])
    filename = 'trouwtokenized' + str(year) + '.json'
    text = prepro.selecttxt(article)
    if text != '':
        tokens = prepro.tokenize(text)
        with open(filename, 'a') as newfile:
            newfile.write('\n')
            json.dump(tokens, newfile)
            anytext += 1
        if counter % 5 == 0:
            print(str(counter) + "/262167")
    else:
        nnotext += 1
    
    
with open('trouwtokenized.json','a') as newfile:
    newfile.write(']')

print(nnotext)
print(anytext)

f.close()




if __name__ == '__main__':
    pass