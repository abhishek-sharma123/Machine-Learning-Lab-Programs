# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 20:34:01 2021

@author: thebe
"""



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

msg = pd.read_csv("naivetext.csv", names=["message", "label"])
print("The dimensions of the dataset", msg.shape)
msg["labelnum"] = msg.label.map({"pos": 1, "neg": 0})
X = msg.message
y = msg.labelnum

xtrain, xtest, ytrain, ytest = train_test_split(X, y)
print(xtest.shape)
print(xtrain.shape)
print(ytest.shape)
print(ytrain.shape)
print("train data")
print(xtrain)

count_vect = CountVectorizer()
xtrain_dtm = count_vect.fit_transform(xtrain)
xtest_dtm = count_vect.transform(xtest)
print(count_vect.get_feature_names())
df = pd.DataFrame(xtrain_dtm.toarray(), columns=count_vect.get_feature_names())
print(df)  
print(xtrain_dtm)  

clf = MultinomialNB().fit(xtrain_dtm, ytrain)
predicted = clf.predict(xtest_dtm)

print("Accuracy metrics")
print("Accuracy of the classifer is", metrics.accuracy_score(ytest, predicted))
print("Confusion matrix")
print(metrics.confusion_matrix(ytest, predicted))
print("Recall and Precison ")
print(metrics.recall_score(ytest, predicted))
print(metrics.precision_score(ytest, predicted))