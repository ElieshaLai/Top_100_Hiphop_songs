# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:33:16 2020

@author: USER
"""


import re
import numpy as np
import pandas as pd
import spacy
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


#read file
df = pd.read_csv(r"hot100_rnb_hiphop_2000s_clean.csv", encoding ="latin-1") 
df.fillna("",inplace=True)


#remove stopwords


from nltk.corpus import stopwords
stops = set(stopwords.words("english"))                  
df["lyrics"] = df["lyrics"].str.lower().str.split()
df["lyrics"].apply(lambda x: [item for item in x if item not in stops])


speech_list = list(df["lyrics"])
speech_list =[" ".join(review) for review in df["lyrics"].values]

n_topics = 10  
n_top_words = 50 

tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2,
                                stop_words='english',max_features=500)
tf = tf_vectorizer.fit_transform(speech_list)
lda = LatentDirichletAllocation(n_components=n_topics, max_iter=50,
                                learning_method='online',
                                learning_offset=50.,
                                random_state=0)
lda.fit(tf)

feature_names = tf_vectorizer.get_feature_names()
compoments = lda.components_

#to excel
topic_dic = {}
for no in range(n_topics):
  topic = ([feature_names[i] for i in compoments[no].argsort()[:-n_top_words - 1:-1]])
  topic_dic["topic"+str(no+1)] = topic

topic_df = pd.DataFrame(topic_dic)
topic_df.to_csv (r'C:\Users\USER\Desktop\topics.csv', index=False)  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    