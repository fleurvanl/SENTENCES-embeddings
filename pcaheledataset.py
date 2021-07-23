# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 15:49:25 2021

@author: aluenen
"""

import gensim
from gensim.models.word2vec import Word2Vec
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
import matplotlib.pyplot as plt

my_words = ['kanker', 'borstkanker', 'longkanker', 'alzheimer', 'prostaatkanker',\
            'reuma', 'tuberculose', 'tbc', 'ziekte', 'malaria', 'suikerziekte']


w2v = Word2Vec.load("D:/Newsdata/Models/compass.model")

my_vocab = {}
  
for w in w2v.wv.vocab:
    my_vocab[w] = w2v.wv[w]
       
df = pd.DataFrame.from_dict(my_vocab, orient='index')

print(df.head)
    
x = StandardScaler().fit_transform(df)

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
print(principalComponents.shape)
print(principalComponents)

#find index of target words
#https://thispointer.com/python-find-indexes-of-an-element-in-pandas-dataframe/

def getIndexes(dfObj, value):
    ''' Get index positions of value in dataframe i.e. dfObj.'''
    listOfPos = list()
    # Get bool dataframe with True at positions where the given value exists
    result = dfObj.isin([value])
    # Get list of columns that contains the value
    seriesObj = result.any()
    columnNames = list(seriesObj[seriesObj == True].index)
    # Iterate over list of columns and fetch the rows indexes where value exists
    for col in columnNames:
        rows = list(result[col][result[col] == True].index)
        for row in rows:
            listOfPos.append((row, col))
    # Return a list of tuples indicating the positions of value in the dataframe
    return listOfPos

#finding one single item
listOfPositions = getIndexes(df, 'kanker')
print('Index positions of "kanker" in Dataframe : ')
for i in range(len(listOfPositions)):
    print('Position ', i, ' (Row index , Column Name) : ', listOfPositions[i])

#going through multiple items
#dictOfPos = {elem: getIndexes(df, elem) for elem in my_words}
#print('Position of given elements in Dataframe are : ')
#for key, value in dictOfPos.items():
#    print(key, ' : ', value)

#turn vocab column of df into a series to find the indexes of each word in principal components
#ser1 = df.ix[:,0]


#for word in my_words:
#    pass

#collect the principal components for each word
#...


    
#plot principal components
X = principalComponents[:,0]#first column
Y = principalComponents[:,1]#second column

plt.scatter(X, Y)
for i, txt in enumerate(my_words):
    print(txt, X[i], Y[i])
    plt.annotate(txt, (X[i], Y[i]))

plt.show()