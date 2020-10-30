# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 22:07:13 2020

@author: USER
"""

from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 
  
# Reads 'Youtube04-Eminem.csv' file  
df = pd.read_csv(r"hot100_rnb_hiphop_2000s_clean.csv", encoding ="latin-1") 
  
comment_words = '' 
stopwords = set(STOPWORDS)
mask=df['year']<2020
mask2=2015<df['year']
two=df[mask][mask2]['lyrics']


  
# iterate through the csv file 
for val in two: 
      
    # typecaste each val to string 
    val = str(val) 
  
    # split the value 
    tokens = val.split() 
      
    # Converts each token into lowercase 
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower() 
      
    comment_words += " ".join(tokens)+" "
  
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words) 
  
# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 