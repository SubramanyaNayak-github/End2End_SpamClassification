import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB




df = pd.read_csv('spam.csv',encoding = 'latin-1')

df.drop(['Unnamed: 2','Unnamed: 3','Unnamed: 4'],axis =1, inplace = True)

df['class']= df['class'].map({'ham':0,'spam':1})

X = df['message']
y = df['class']


cv = CountVectorizer()

# Fit the Data
X = cv.fit_transform(X)

pickle.dump(cv, open('tranform.pkl', 'wb'))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

#Naive Bayes Classifier
from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB()
clf.fit(X_train,y_train)
clf.score(X_test,y_test)

filename = 'nlp_model.pkl'
pickle.dump(clf, open(filename, 'wb'))



