#!/usr/bin/python36

def save_in_database():
	pass
import subprocess as sp
import cgi,cgitb
import os

cgitb.enable()
print("content-type: text/html")
print()


data=cgi.FieldStorage()
ip= data.getvalue('ip')


a=sp.getoutput("sudo sshpass -p redhat  ssh-copy-id {}".format(ip))
print(a)