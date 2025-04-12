import string 
import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwards
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

nltk.download()

df = pd.read_csv('spam_ham_dataset.csv')
df['text'] = df['text'].apply(lambda x: x.replace('\r\n', ' '))
df.info()

stemmer = PorterStemmer()
stemmer.stem('sophistication')
corpus = []

stopwords_set = set(stopwords.words('english'))


for i in range(len(df)):
    text = df['text'].iloc[i].lower()
    text = text.translate(str.maketrans('', '', string.punctuation)).split()
    text = [stemmer.stem(word) for word in text if word not in stopwords_set]
    text = ' '.join(text)
    corpus.append(text)