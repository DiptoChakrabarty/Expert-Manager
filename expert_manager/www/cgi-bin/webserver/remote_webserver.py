#!/usr/bin/python36

import subprocess as sp
import cgi
import os
print("content-type: text/html")
print()

def write_data(ip,username,password):
	pass	
	

data=cgi.FieldStorage()
ip=data.getvalue('ip')
username=data.getvalue('username')
password=data.getvalue('password')

print(ip)
f=open('../hosts','r+')
f.write('[web]\n')
f.write('{} ansible_user={} ansible_password={}\n'.format(ip,username,password))
f.close()
#a1=sp.getoutput("sudo echo '' | cat > hosts")
#print(a1)	
#a2=sp.getoutput("sudo sshpass -p {} ssh-copy-id {}@{}".format(password,username,ip))
#a3=sp.getoutput("sudo echo '{} ansible_user={} ansible_password={}' | cat >> hosts".format(ip,username,password))
#print(a2)
#print(a3)
a=sp.getoutput("sudo ansible-playbook -i ../hosts ../playbooks/webserver.yml")
print(a)

#rint(a)
print("location: http://{}/myserver.html".format(ip))

5