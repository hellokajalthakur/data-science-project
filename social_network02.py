# -*- coding: utf-8 -*-
"""Untitled18.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qALmGeuZQl-vn6wdgI7KFnhm7iel_LhU
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path='//content/social_network.csv'
data=pd.read_csv(path)
data.head()

from sklearn import preprocessing
le=preprocessing.LabelEncoder()
data['Gender']=le.fit_transform(data['Gender'])

data.head()

X=data[['Age','EstimatedSalary','Gender']]
Y=data['Purchased']
print(X,Y)

#split X and Y into training and testing sets
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)
print(X_train)
print(X_test)

#import the class
from sklearn.linear_model import LogisticRegression
#instantiate the model(using the default parameters)
logreg=LogisticRegression()
#fit the model with data
logreg.fit(X_train,Y_train)
Y_pred =logreg.predict(X_test)
print(Y_pred)
print(Y_test)

#import the metrics class
from sklearn import metrics
cnf_matrix=metrics.confusion_matrix(Y_test,Y_pred)
cnf_matrix

# Commented out IPython magic to ensure Python compatibility.
#import required modules
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

class_name=[0,1] # name of classes
fig, ax = plt.subplots()
tick_marks=np.arange(len(class_name))
plt.xticks(tick_marks, class_name)
plt.yticks(tick_marks, class_name)
print
# create heatmap
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="Greens" ,fmt='d', annot_kws={"size":10})
ax.xaxis.set_label_position("bottom")
plt.tight_layout()
plt.title('Confusion matrix',y=1.4)
plt.xlable('Actual lable')
plt.ylable('Predicted lable')

print("Accuracy:",metrics.accuracy_score(Y_test,Y_pred))
print("Precision:",metrics.precision_score(Y_test,Y_pred))
print("Recall:",metrics.recall_score(Y_test,Y_pred))
print("F1 score:",metrics.f1_score(Y_test,Y_pred))