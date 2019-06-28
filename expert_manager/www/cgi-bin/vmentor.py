#!/usr/bin/python36

import subprocess as sp
import cgi
import os
print("content-type: text/html")
print('location: http://192.168.43.217/vmentor.html')
print()

data=cgi.FieldStorage()
profile_name=data.getvalue('profile_name')
input_data=data.getvalue('input_data')
#profile_name='arpit'
print(profile_name)
print(input_data)
a=sp.getoutput('pwd')
print(a)
#input_data='dadada'
import sqlite3

connection= sqlite3.connect('./mydata.db')

crsr=connection.cursor()

#sql_command= 'create table {} (input_data varchar(80) ); '.format(profile_name)
#crsr.execute(sql_command)

crsr.execute("insert into {} values (?)".format(profile_name),(input_data,))

connection.commit()
connection.close()

#print(ip)