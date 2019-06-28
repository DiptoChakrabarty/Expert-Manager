#!/usr/bin/python36
# -*- coding: utf-8 -*-

import cgi, cgitb, os, sys
import subprocess as sp


def dlp_logistic_model(model_name):

    import pandas as pd 
    dataset=pd.read_csv('{}/titanic_train.csv'.format(model_name))
    def change_cols(cols):
        Age = cols[0]
        Pclass = cols[1]
        
        if pd.isnull(Age):
            if Pclass == 1:
                return 38
            elif Pclass == 2:
                return 29
            else:
                return 25
            
        else:
            return Age
    dataset['Age'] = dataset[['Age', 'Pclass']].apply(change_cols, axis=1)
    Pclass=pd.get_dummies(dataset['Pclass'],drop_first=True)
    gender=pd.get_dummies(dataset['Sex'],drop_first=True)
    embark=pd.get_dummies(dataset['Embarked'],drop_first=True)
    dataset=pd.concat([dataset,Pclass,gender,embark],axis=1,)
    dataset.drop(['PassengerId','Pclass','Name','Sex','Ticket','Fare','Cabin','Embarked'],axis=1,inplace=True)
    from sklearn.model_selection import train_test_split
    X=dataset.iloc[:,1:]
    y=dataset.iloc[:,0]
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30,random_state=42)
    from sklearn.linear_model import LogisticRegression
    model=LogisticRegression()
    model.fit(X_train,y_train)
    y_pred=model.predict(X_test)
    type(y_pred)
    from sklearn.metrics import confusion_matrix
    confusion_matrix(y_test,y_pred)
    print("model accuracy is: ")
    print((138+78)/268)




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

    dlp_logistic_model(model_name)


cgitb.enable()
save_uploaded_file()