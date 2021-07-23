# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 12:16:35 2021

@author: aluenen
"""

import gensim
from gensim.models.word2vec import Word2Vec
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
import matplotlib.pyplot as plt
import os
print(os.getcwd())
import statistics
import numpy as np
from matplotlib import pyplot
#figure out if the distances are normally distributed
#compass = Word2Vec.load("D:/Newsdata/Models/compass.model")

alldist = []

for year in range(2010, 2019):
    for part in range(1, 3):
        yearpart = str(year) + '_' + str(part)
        filename = "D:/Newsdata/Models/" + yearpart + '.model'
        w2v = Word2Vec.load(filename)
        distances = []
        for word in w2v.wv.vocab.keys():
            alldist.append(w2v.wv.similarity('kanker', word))

        

pyplot.hist(alldist)
pyplot.show()