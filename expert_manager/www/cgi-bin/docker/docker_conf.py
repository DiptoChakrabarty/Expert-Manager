#!/usr/bin/python36
import subprocess

print("content-type: text/html")
print()


cmd = "sudo docker ps -a"

output = subprocess.getoutput(cmd)


container_list = output.split("\n")
print("<a target=mydocker href='docker_input.py'>Click to launch new docker container</a><br/>")
print("<iframe width='100%' name='mydocker'></iframe>")

print("<iframe width='100%' name='myconsole'></iframe>")

print("""
<table border='5' width='100%'>
<tr>
<th>Container Name</th>
<th>Image Name</th>
<th>Status</th>
<th>Start</th>
<th>Stop</th>
<th>Terminate</th>
<th>Console</th>
</tr>""")

for c  in container_list[1:]:
	if "Up" in c:
		cstatus = "running"
	elif  "Exited" or 'Created' in c:
		cstatus = "stopped"
	else:
		status = "unknown status"
	c_details  =  c.split()
	cname =  c_details[-1]
	imagename = c_details[1]
	port_shell= c_details[-2]
	port_shell=port_shell[8:12]
	#print(port_shell)
	string='{print$2}'
	doc_ip=subprocess.getoutput("sudo docker inspect {0} | grep -i ipaddress | sed -n '2 p' | awk {1} ".format(cname,string))
	doc_ip=doc_ip.split(':')
	doc_ip=doc_ip[1]
	doc_ip=doc_ip[:len(doc_ip)-1]
	doc_ip=doc_ip[2:-1]	
	print('''

	<tr>
	<td>{}</td>
	<td>{}</td>
	<td>{}</td>
	<td><a href='http://192.168.43.217/cgi-bin/docker/docker_start.py?s={}'>Start</a></td>
	<td><a href='http://192.168.43.217/cgi-bin/docker/docker_stop.py?s={}'>Stop</a></td>
	<td><a href='http://192.168.43.217/cgi-bin/docker/docker_remove.py?s={}'>Terminate</a></td>
	<td><a target='myconsole' href='http://192.168.43.217:{}'>Console</a></td>
	</tr>
	'''.format(cname, imagename, cstatus, cname, cname, cname, port_shell ))



print("</table>")


