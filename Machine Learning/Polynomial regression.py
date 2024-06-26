# -*- coding: utf-8 -*-
"""Polynomial ML

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NoEvT4Nt2_3iLcWXBlxDigV4X05S4Rbe
"""

import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import r2_score
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

url="https://raw.githubusercontent.com/jadijadi/machine_learning_with_python_jadi/main/FuelConsumption.csv"
d=pd.read_csv(url)
d

mask=np.random.rand(len(d))<0.8 # 80% True, 80 is for train.
mask
print(len(d))
train=d[mask]
print(len(train))
test=d[~mask]
print(len(test))

train_x=train[['ENGINESIZE']]
b=[]
l=[]
for n in range(2,20):
 l.append(n)
 p=PolynomialFeatures(degree=n)
 train_x_p=p.fit_transform(train_x)
 train_y=train[['CO2EMISSIONS']]
 r=linear_model.LinearRegression()
 r.fit(train_x_p,train_y)
 a=r.coef_
 c=r.intercept_
 print("coefficint is",a,"and the intercept is",c)
 test_x=test[['ENGINESIZE']]
 test_x_p=p.fit_transform(test_x)
 test_y=test[['CO2EMISSIONS']]
 test_p=r.predict(test_x_p)
 r2=r2_score(test_p,test_y)
 print(r2)
 b.append(r2)
d=max(b)
f=b.index(d)
print(f)
print(l[f])
u=(l[f])

fig=plt.figure()
ax=fig.add_subplot()
ax.set_xlabel("Degree")
ax.set_ylabel("R2")
ax.scatter(l,b)

print(train_x)
train_x_p

p=PolynomialFeatures(degree=u)
train_x_p=p.fit_transform(train_x)
train_y=train[['CO2EMISSIONS']]
r=linear_model.LinearRegression()
r.fit(train_x_p,train_y)
a=r.coef_
c=r.intercept_

fig=plt.figure()
ax=fig.add_subplot()
ax.scatter(train['ENGINESIZE'],train['CO2EMISSIONS'],color="blue")
ax.scatter(test['ENGINESIZE'],test['CO2EMISSIONS'],color="green")
ax.set_xlabel("Engine size")
ax.set_ylabel("CO2 Emission")
ax.set_title("The CO2 emission chart")
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
x=np.arange(1,9,0.1)
plt.plot(x,a[0][1]*x+a[0][2]*x**2+a[0][3]*x**3+c)

test_x=test[['ENGINESIZE']]
test_x_p=p.fit_transform(test_x)
test_y=test[['CO2EMISSIONS']]
test_p=r.predict(test_x_p)
r2=r2_score(test_p,test_y)
print(r2)