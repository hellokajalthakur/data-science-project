# -*- coding: utf-8 -*-
"""datasci.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UpRAhtvmo5eG94JcQjxDlZZfRzg_a67X
"""

import pandas as pd

path='//content/headbraiin.csv'
df=pd.read_csv(path)
df.head()
print(df)

import numpy as np
import matplotlib.pyplot as plt

x = df['Head Size(cm^3)'].values
y = df['Brain Weight(grams)'].values
print(x,y)

plt.scatter(x, y, color='green')
plt.plot(x, y, color='red')
plt.title('Simple Linear Regression')
plt.xlabel('Head size cm^3')
plt.ylabel('Brain weight in grams')