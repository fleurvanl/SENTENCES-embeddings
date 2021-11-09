# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 15:49:25 2021

@author: aluenen
"""
#THIS CODE IS WORKING! it does only do the pca and then saves it for memory reasons
#the PCA of my self-trained embeddings is here: D:/Code/SENTENCES-embeddings/pca_w2v_300_10_15.model.npy
#and can be loaded to be visualised elsewhere (see file topicvisualisatie_PCAfullembed.py)
import gensim
import gensim.downloader
from gensim.models.word2vec import Word2Vec
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
import matplotlib.pyplot as plt
import numpy as np

#my_words = ['kanker', 'borstkanker', 'longkanker', 'alzheimer', 'prostaatkanker',\
#            'reuma', 'tuberculose', 'tbc', 'ziekte', 'malaria', 'suikerziekte']

#my_words = ['delicious', 'yummy', 'tasty', 'disgusting', 'bland',\
#            'jump', 'run', 'step', 'slip', 'jumped', 'ran', 'stepped', 'slipped',\
 #               'wall', 'fence', 'door',\
 #                   'banana', 'apple', 'kiwi', 'bananas', 'apples', 'kiwis']

target_words = ['king', 'queen', 'man', 'woman']    
    
w2v = Word2Vec.load("D:/Newsdata/Models/uncased/300_10_15.model")
#w2v = gensim.downloader.load('word2vec-google-news-300')

#my_vocab = {}
my_words = []
my_embeddings = []
  
for w in w2v.wv.vocab:
    #my_vocab[w] = w2v.wv[w]
    my_words.append(w)
    my_embeddings.append(w2v.wv[w])
       
df = pd.DataFrame(my_embeddings)#.from_dict(my_vocab, orient='index')

#print(df.head)
    
x = StandardScaler().fit_transform(df)

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
print(principalComponents.shape)
#print(principalComponents)

np.save("pca_w2v_300_10_15.model", principalComponents)
    
#plot principal components
#X = principalComponents[:,0]#first column
#Y = principalComponents[:,1]#second column

#plt.scatter(X, Y)
#for i, txt in enumerate(my_words):
#    print(txt, X[i], Y[i])
#    plt.annotate(txt, (X[i], Y[i]))

#plt.show()
#plt.savefig("pcamankingwomanqueen")