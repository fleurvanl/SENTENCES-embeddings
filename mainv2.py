# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 15:05:13 2021

@author: aluenen
"""

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
from nltk import sent_tokenize
from preprocessing import Preprocessing
prepro = Preprocessing()

#nog doen: telegraaf & volkskrant

os.chdir('D:/Newsdata')
print("Current Working Directory " , os.getcwd())

f = open('nrc (print).json', 'r')
print('file opened')

nnotext = 0
anytext = 0
counter = 0
faulty = []

for line in f:
    article = json.loads(line)
    date = article["publication_date"]
    year = int(date[:4])
    if year > 2009:
        #filename = 'trouwtokenized' + str(year) + '.json'
        text = prepro.selecttxt(article)
        sentences = sent_tokenize(text, language="dutch")
        if text != '':
            counter += 1
            tokens = prepro.tokenize(sentences) #list of strings per sentence
            #print('tokens type =', type(tokens))
            with open("nrc20102018.txt", 'a') as newfile:
                for sentence in tokens:
                    ssentence = sentence + '\n'
                    try:
                        newfile.write(ssentence)
                    except UnicodeEncodeError:
                        faulty.append(ssentence)
                #newfile.write('\n')
                #json.dump(tokens, newfile)
                anytext += 1
            if counter % 5 == 0:
                print(str(counter) + "/311174")
        else:
            nnotext += 1
    
    


print(nnotext)
print(anytext)
print('UnicodeEncodeError:')
print(faulty)

f.close()




if __name__ == '__main__':
    pass