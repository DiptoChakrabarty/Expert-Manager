#!/usr/bin/python36
# -*- coding: utf-8 -*-

import cgi, cgitb, os, sys
import subprocess as sp

def dlp_linear_model(model_name):


    from keras.models import Sequential


    model = Sequential()

    from keras.layers import Dense


    model.add(Dense(units=1, input_shape=(1,)))

    model.summary()

    from keras.optimizers import Adam, SGD

    model.compile(optimizer=Adam(),loss='mean_squared_error')


    import pandas as pd
    dataset=pd.read_csv('{}/weight-height.csv'.format(model_name))


    X=dataset.iloc[:,1]

    y=dataset.iloc[:,-1]



    model.fit(X,y,epochs=50,verbose=0)



    y_predict=model.predict(X)


    from sklearn.metrics import mean_absolute_error
    error=mean_absolute_error(y,y_predict)






    from sklearn.linear_model import LinearRegression



    model=LinearRegression()

    X_new=dataset.iloc[:,1:2]

    model.fit(X_new,y)

    pred=model.predict(X_new)

    error=mean_absolute_error(y,pred)

    print("</br>")
    print("Mean Squre Error")
    print(error)



def save_uploaded_file():
    print('Content-Type: text/html; charset=UTF-8')
    print()
    print('''
    <html>
    <head>
    <title>Upload File</title>
    </head>
    <body>
        ''')

    form = cgi.FieldStorage()
    model_name=form.getvalue('model_name')
    sp.getoutput("sudo mkdir {}".format(model_name))
    sp.getoutput("sudo chmod 777 {}".format(model_name))

    UPLOAD_DIR = './{}'.format(model_name)

        
    form_file = form['file']

    if not form_file.filename:
        print('<h1>Not found parameter: file</h1>')
        return

    uploaded_file_path = os.path.join(UPLOAD_DIR, os.path.basename(form_file.filename))
    with open(uploaded_file_path, 'wb') as fout:
        while True:
            chunk = form_file.file.read(100000)
            if not chunk:
                break
            fout.write (chunk)

    dlp_linear_model(model_name)

cgitb.enable()
save_uploaded_file()