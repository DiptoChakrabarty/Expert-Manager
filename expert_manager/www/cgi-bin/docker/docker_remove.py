#!/usr/bin/python36

import subprocess as sp
import cgi
import os
print("content-type: text/html")
print("location: http://192.168.43.217/cgi-bin/docker/docker_conf.py")
print()


data=cgi.FieldStorage()
docker_name=data.getvalue('s')

a=sp.getoutput("sudo docker rm -f {}".format(docker_name))
