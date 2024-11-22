# -*- coding: utf-8 -*-
"""LinearRegression_LSM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QfroQ58EUi1x7OqKMat1ZED6m9yEIRrL
"""

import numpy as np #numerical python # n_Dim array
import matplotlib.pyplot as plt #plotting

x=[1,2,3,4,5]
y=[2,4,5,4,5]

#mean_x, mean_y
n =len(x)
mean_x = np.mean(x)
mean_y = np.mean(y)
print(mean_x)
print(mean_y)
#print(n)

numer = 0
denon = 0
for i in range(n):
  numer = numer + (x[i]-mean_x)*(y[i]-mean_y)
  denon = denon + (x[i]-mean_x)**2
  m = numer/denon
  c = mean_y - (m*mean_x)
  print(m)
  print(c)

plt.scatter(x,y, colour='red')
plt.plot(x,y, colour='blue')

max_x= np.max(x)+5
min_x = np.min(x)-5