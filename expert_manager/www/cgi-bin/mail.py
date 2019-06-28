#!/usr/bin/python36

def save_in_database():
	pass
import subprocess as sp
import cgi
import os
print("content-type: text/html")
print()

data=cgi.FieldStorage()
username_sender= data.getvalue('username_sender')
password= data.getvalue('password')
username_receiver=data.getvalue('username_receiver')
subject=data.getvalue('subject')
body=data.getvalue('body')


f=open('hosts','r+')
f.write('[localhost]\n')
f.write('127.0.0.1 ansible_user=root ansible_password=redhat\n')
f.close()


f=open('playbooks/data.yml','r+')
f.write('mail_id_sender: {}\n'.format(username_sender))
f.write("password: '{}'\n".format(password))
f.write("mail_id_receiver: '{}'\n".format(username_receiver))
f.write("subject: '{}'\n".format(subject))
f.write("body: '{}'\n".format(body))
f.close()

a=sp.getoutput("sudo ansible-playbook playbooks/mail.yml")
print(a)
print("Successfully sent mail")