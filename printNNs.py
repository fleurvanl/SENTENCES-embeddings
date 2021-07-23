# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 11:14:38 2021

@author: aluenen
"""

import gensim
from gensim.models.word2vec import Word2Vec
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
import matplotlib.pyplot as plt

w2v = Word2Vec.load("D:/Newsdata/Models/compass.model")


#10 nearest neighbours van kanker die GEEN kankersoort zijn
#my_words = ['kanker', 'alzheimer', 'leukemie', 'ziekte', 'reuma', 'suikerziekte',\
#              'tuberculose', 'aids', 'malaria', 'epilepsie', 'hiv']
#nearest neighbours die wél kankersoorten zijn
my_words = ['kanker', 'borstkanker', 'longkanker', 'alzheimer', 'prostaatkanker',\
            'reuma', 'tuberculose', 'tbc', 'ziekte', 'malaria', 'suikerziekte']


#(w2v.wv.vocab.keys())
    
my_vocab = {}
for w in my_words:
    my_vocab[w] = w2v.wv[w]#w2v.wv.vocab[w]
    
    
df = pd.DataFrame.from_dict(my_vocab, orient='index')

print(df.head)
    
x = StandardScaler().fit_transform(df)

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
print(principalComponents.shape)
print(principalComponents)

X = principalComponents[:,0]#first column
Y = principalComponents[:,1]#second column

plt.scatter(X, Y)
for i, txt in enumerate(my_words):
    print(txt, X[i], Y[i])
    plt.annotate(txt, (X[i], Y[i]))

plt.show()