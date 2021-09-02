# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 17:16:43 2021

@author: aluenen
"""

import gensim
from gensim.models.word2vec import Word2Vec
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
import os
print(os.getcwd())


model = Word2Vec.load("D:/Newsdata/Models/uncased/2018_2.model")

print(len(model.wv.vocab))