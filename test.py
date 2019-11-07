import os
import glob
from pathlib import Path, PurePath
import numpy as np
import pandas as pd
from pprint import pprint
import copy
import random as rd
from itertools import permutations

import nltk
from nltk.stem import arlstem
arl = arlstem.ARLSTem()
from nltk.stem import isri
isri_stem = isri.ISRIStemmer()
nltk.download('punkt')
nltk.download('stopwords')

import gensim
import gensim.corpora as corpora
from gensim.models import CoherenceModel

import pyLDAvis
import pyLDAvis.gensim
import matplotlib.pyplot as plt
%matplotlib inline


path = PurePath('~/Users/UCD/Documents/Topic Modeling')
parent = PurePath('C:/Users/UCD/Documents/Topic Modeling/watan-2004') 

texts = []

subdirs = [PurePath(x[0]) for x in os.walk(path)]
topic = ''

for subdir in subdirs:
    if subdir.parent == parent:
        topic = subdir.parts[-1]
        os.chdir(subdir)
        text_list = glob.glob("*.html")
        for k in range(min(len(text_list), 5000)):
            text_file = text_list[k]
            with open(text_file, 'r', encoding = 'utf8') as file:
                text = file.read()
            texts.append((text, topic))
            
raw_texts_df = pd.DataFrame(data = texts, columns = ['Text', 'Topic'])