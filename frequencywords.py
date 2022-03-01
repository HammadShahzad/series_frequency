import pandas
import pandas as pd
import numpy as np
import regex as re
import squarify
from collections import Counter
import matplotlib.pyplot as plt


import csv

data = pd.read_csv('survey_final.csv',names=['col1','col2','col3','col4','col5','col6','col7'])
suggestions = data.iloc[:,5]
fsuggestions = suggestions.str.strip().str.replace('[^\w\s]',' ',regex=True).str.lower().str.replace(",", " ", regex=True)
fsuggestions = fsuggestions.str.replace(".", " ", regex=True).str.replace('!', ' ', regex=True)
sugges_freqone=Counter(" ".join(fsuggestions).split()).most_common(900)
sugges_freqtwo=pd.DataFrame(sugges_freqone,columns=['Word','Frequency'])
sugges_freqtwo.plot(x='Word',y='Frequency',kind='bar')
print(sugges_freqtwo)
sugges_freqtwo.to_csv('final_freq0_1.csv')



