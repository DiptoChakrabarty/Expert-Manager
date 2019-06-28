#!/usr/bin/python36

import subprocess as sp
import cgi
import os
print("content-type: text/html")
#print('location: http://192.168.43.217/cgi-bin/docker_input.py')
print()

data=cgi.FieldStorage()
docker_no= data.getvalue('docker_no')


print("<form action='docker/docker_input.py'>")
l=[]
for i in range(int(docker_no)):
	l.append(0)
	print("<label>Enter docker {} name</label></br>".format(i+1))
	print("<input type='text' name='{}'></br>".format(i+1))
	l[i]=i+1
print("<button>Submit</button>")
	
print("</form>")