# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 11:23:08 2021

@author: aluenen
"""
import spacy
nlp = spacy.load('nl_core_news_sm')
from nltk import sent_tokenize


class Preprocessing():
    def __init__(self):
        pass
    
    def selecttxt(self, article):
        text = ''
        try:
            text = text + ' ' + article['text']
        except:
            pass
        try:
            text = text + ' ' + article['byline']
        except:
            pass
        try: #in case of title there is often a "VOLLEDIGE TEKST" part
            text = text + ' ' + article['title']
        except:
            pass 
        #try: #this is preprocessed data
        #    text = text + ' ' + article['cosine_processed']
        #except:
        #    pass
        return text


    def tokenize(self, sentences):
        words = []
        for sentence in sentences:
            newsent = []
            newwords = nlp(sentence)
            for token in newwords:
                newsent.append(str(token))
            newsentence = ' '.join(newsent)
            #print('newsentence type =', type(newsentence))
            words.append(newsentence)
        return words

       



