# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 08:56:46 2021

@author: aluenen
"""

import gensim
import gensim.downloader
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

#wv = Word2Vec.load("D:/Newsdata/Models/uncased/volkskrant.model")
wv = gensim.downloader.load('glove-twitter-200')

for item in wv.most_similar('cancer', topn=30):
    print(item)

