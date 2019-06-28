#!/usr/bin/python36

import subprocess as sp
import cgi
import os

print("content-type: text/html")
print()
b=sp.getoutput("echo '[web]' | cat > hosts")
c=sp.getoutput("echo '127.0.0.1 ansible_user=root ansible_password=redhat' | cat >> hosts")
f=open('hosts','r+')
f.write('[web]\n')
f.write('127.0.0.1 ansible_user=root ansible_password=redhat\n')
f.close()
a=sp.getstatusoutput("sudo ansible-playbook -i ../hosts ../playbooks/webserver.yml")
print(a)
#print(a)
