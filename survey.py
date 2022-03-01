import pandas
import pandas as pd
import numpy as np
import regex as re
import squarify
from collections import Counter
import matplotlib.pyplot as plt

import csv

data = pd.read_csv('survey_final.csv', names=['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7'])
suggestions = data.iloc[:, 5]
fsuggestions = suggestions.str.strip().str.lower().str.replace(",", "", regex=True)
fsuggestions = fsuggestions.str.replace(".", "", regex=True).str.replace('!', '', regex=True)
fsuggestions['frequency'] = fsuggestions.str.count('study hours')
print("Fre: ",fsuggestions['frequency'].sum())
