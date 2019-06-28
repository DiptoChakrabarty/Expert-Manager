#!/usr/bin/python36

def save_in_database():
	pass
import subprocess as sp
import cgi
import os
print("content-type: text/html")
print("location: http://192.168.43.217/cgi-bin/docker_conf.py")
print()

data=cgi.FieldStorage()
number= data.getvalue('number')
msg= data.getvalue('msg')

f=open('hosts','r+')
f.write('[sms]\n')
f.write('127.0.0.1 ansible_user=root ansible_password=redhat\n')
f.close()

number=" '{}' ".format(number)
print(number)
f=open('playbooks/data.yml','r+')
f.write('number: {}\n'.format(number))
f.write("msg: '{}'\n".format(msg))
f.close()

a=sp.getoutput("sudo ansible-playbook playbooks/message.yml")
