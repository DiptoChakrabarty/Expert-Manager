#!/usr/bin/python36

def save_in_database():
	pass
import subprocess as sp
import cgi
import os
print("content-type: text/html")


data=cgi.FieldStorage()
docker_name= data.getvalue('docker_name')

import random
random_num= random.randint(1000,9999)
a=sp.getoutput("sudo docker run -p {}:4200 -itd --name {}  -v /run/media/root/RHEL-7.5\ Server.x86_64:/dvd -v /root/rhel7_5_rpm_extras:/rpm -v /root/rhel7_extra_new_rpm:/new_rpm -v /root/python_lib:/python_lib -v /tmp/.X11-unix:/tmp/.X11-unix shell:v3".format(random_num,docker_name))
#a=sp.getoutput("sudo ansible-playbook -i ../hosts playbooks/launch_container.py")
#b=sp.getoutput("sudo docker cp .bashrc {}:/root/.bashrc".format(docker_name))
#c=sp.getoutput("sudo docker restart {}".format(docker_name))

print("location: http://192.168.43.217/cgi-bin/logs.py?docker_name={}".format(docker_name))
print()

#print("<input type='hidden' name='docker_name' value={}>".format(docker_name))
