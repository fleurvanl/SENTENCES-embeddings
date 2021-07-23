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
import os
print(os.getcwd())

#compass = Word2Vec.load("D:/Newsdata/Models/compass.model")

#print(compass.wv.most_similar('kanker', topn=20))

#10 nearest neighbours van kanker die GEEN kankersoort zijn
compassnns = ['alzheimer', 'ziekte', 'reuma', 'suikerziekte',\
              'tuberculose']#, 'aids', 'malaria', 'epilepsie', 'hiv']
 
#10 nearest neighbours borstkanker
#compassnns = ['suikerziekte', 'alzheimer', 'reuma', 'trombose', 'anorexia']

#10 nearest neighbours darmkanker
#compassnns = ['trombose', 'hartfalen', 'suikerziekte', 'melanoom', 'aderverkalking']

#nearest neighbours baarmoederhalskanker
#compassnns = ['taaislijmziekte',  'HPV', 'hiv', 'kinkhoest', 'melanoom', 'trombose']
   
data = {}
#structure data {woord:[cossim, cossim], woord:[cossim, ]}
 
for year in range(2010, 2019):
    for part in range(1, 3):
        yearpart = str(year) + '_' + str(part)
        filename = "D:/Newsdata/Models/" + yearpart + '.model'
        #print(filename)
        #try:
        w2v = Word2Vec.load(filename)
        for word in compassnns:
            if word not in data.keys():
                data[word] = [w2v.wv.similarity('kanker', word)]
            else:
                data[word].append(w2v.wv.similarity('kanker', word))
        #except:
        #    print(yearpart)
        #    for word in compassnns:
        #        if word not in data.keys():
        #            data[word] = [None]
        #        else:
        #            data[word].append(None)
                
x = []
for year in range(2010, 2019):
    for part in range(1, 3):
        yearpart = str(year) + '_' + str(part)
        x.append(yearpart)
#print(x)
            
for word in data:
    #print(data[word])
    plt.plot(x, data[word], label=word)

plt.xticks(rotation=45)
#ax.set_xticks(['2010_1', '2011_1', '2012_1', '2013_1', '2014_1', '2015_1', \
#              '2016_1', '2017_1', '2018_1'])
#ax.set_xlabels([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018])
#plt.set_xticks([i for i in range(2010, 2019)])    
plt.xlabel('Year') 
plt.ylabel('Cosine similarity') 
plt.ylim(ymax = 1, ymin = 0.5)
plt.title("Cosine similarity between 'kanker' and nearest neighbours") 

#ax = plt.gca()
#print(plt.xticks_marks)

#fix legend
ax = plt.subplot(111)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#plt.legend(loc='lower left')
  
# function to show the plot 
plt.show() 
    
            