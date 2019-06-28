#!/usr/bin/python36

import cgi, cgitb, os, sys
import subprocess as sp



print('Content-Type: text/html; charset=UTF-8')
print()



from keras.models import Sequential


model = Sequential()

from keras.layers import Dense


model.add(Dense(units=1, input_shape=(1,)))

model.summary()

from keras.optimizers import Adam, SGD

model.compile(optimizer=Adam(),loss='mean_squared_error')


import pandas as pd
dataset=pd.read_csv('weight-height.csv')


X=dataset.iloc[:,1]

y=dataset.iloc[:,-1]



model.fit(X,y,epochs=50)



y_predict=model.predict(X)


from sklearn.metrics import mean_absolute_error
error=mean_absolute_error(y,y_predict)



import matplotlib.pyplot as plt

plt.plot(X,y_predict)




from sklearn.linear_model import LinearRegression



model=LinearRegression()

X_new=dataset.iloc[:,1:2]

model.fit(X_new,y)

pred=model.predict(X_new)

error=mean_absolute_error(y,pred)

print(error)