# -*- coding: utf-8 -*-
"""Credit Card Fraud Detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16o5DXZamAiHO4aZzEJ07BATmngI0uhM1

Importing Libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

"""Import google drive"""

from google.colab import drive
drive.mount('/content/drive')

"""Loading data"""

data=pd.read_csv("/content/drive/My Drive/creditcard.csv")
data

"""***Data Exploration***"""

data.describe()

data.head()

data.info()

data.shape

"""***Data Preprocessing***

Finding Missing values
"""

data.isnull().sum()

"""Identification Of Duplicate Records"""

data.duplicated()

"""Removal of duplicates"""

data=data.drop_duplicates()

print(data.shape)
data

fraud_trans=data[data['Class']==1]
valid_trans=data[data['Class']==0]

print("Fraud Transactions:",fraud_trans.shape)

print("Valid Transactions:",valid_trans.shape)

fraud_trans

fraud_trans.Amount.describe()

valid_trans

valid_trans.Amount.describe()

"""***Data Visualization***"""

data.hist(figsize=(50,40),color='blue',edgecolor='black');

plt.plot(data['Class'])
plt.xlabel('Class')
plt.ylabel('levels')
plt.title('Line Plot')
plt.show()

corr_mat=data.corr()
fig=plt.figure(figsize=(9,9))
sns.heatmap(corr_mat, vmax = .9, square = True)
plt.show()

"""***Dividing Input and Output variables***"""

x = data.drop(['Class'], axis = 1)  #feature matrix
y=data['Class']             #dependent variable
xdta=x.values
ydta=y.values
print("Length of feature columns",x.shape)
print("Length of class variable",y.shape)

"""***Split into training and testing data***"""

from sklearn.model_selection import train_test_split
trainX,testX,trainY,testY= train_test_split(xdta,ydta,test_size=0.3,random_state=42)

from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier()
rfc.fit(trainX,trainY)
predictedY=rfc.predict(testX)

"""***Performance Metrics***"""

from sklearn.metrics import classification_report,accuracy_score,precision_score,recall_score,f1_score,confusion_matrix

#Accuracy
print("Accuracy : ", accuracy_score(testY,predictedY))

#Precision
print("Precision : ", precision_score(testY,predictedY))

#Recall
print("Recall : ", recall_score(testY,predictedY))

#f1 score
print("f1 score : ",f1_score(testY,predictedY))

print("Classification Report :\n ",classification_report(testY,predictedY))

LABELS=['Valid','Fraud']
cm=confusion_matrix(testY,predictedY)
plt.figure(figsize=(8,8))
sns.heatmap(cm,xticklabels=LABELS,yticklabels=LABELS,annot=True,fmt="d",cmap="PuBu");
plt.title("Confusion matrix")
plt.ylabel('True class')
plt.xlabel('Predicted class')
plt.show()