#!/usr/bin/python36
f=open('./hadoop_hosts','w')
f.write('')
f.close()

f=open('../hosts','w')
f.write('')
f.close()


def simple_setup_on_all_ips():
	sp.getoutput("sudo ansible-playbook -i ../hosts ../playbooks/hadoop_simple_conf.yml")

def entry_in_host_file(hostname,ip):
	f=open('./hadoop_hosts','a')
	f.write("{} {}\n".format(ip,hostname))
	f.close()

def copy_public_key(password,ip,var_name):
	sp.getoutput("sudo sshpass -p {} ssh-copy-id {}".format(password,ip))
	sp.getoutput("sudo sshpass -p {} ssh {} hostnamectl set-hostname {}".format(password,ip,var_name))

def group_ansible_hosts(ip):
	f=open('../hosts','a')
	f.write('{}\n'.format(ip))
	f.close()
def master_conf():
	sp.getoutput("sudo ansible-playbook -i ../hosts ../playbooks/master_hadoop.yml")
def slave_conf():
	sp.getoutput("sudo ansible-playbook -i ../hosts ../playbooks/slaves_hadoop.yml")
def client_conf():
	sp.getoutput("sudo ansible-playbook -i ../hosts ../playbooks/client_hadoop.yml")
def save_in_database():
	pass
import subprocess as sp
import cgi,cgitb
import os

cgitb.enable()
print("content-type: text/html")
print()


data=cgi.FieldStorage()
m_ips= data.getvalue('m_ips')
s_ips= data.getvalue('s_ips')
c_ips= data.getvalue('c_ips')
m_ips_list=[]
s_ips_list=[]
c_ips_list=[]
m_ips_list_password=[]
s_ips_list_password=[]
c_ips_list_password=[]

f=open('../hosts','a')
f.write('[master]\n')
f.close()
for i in range(int(m_ips)):
	var_name='m'+str(i+1)
	password='m_p'+str(i+1)
	ip=data.getvalue(var_name)
	password=data.getvalue(password)	
	m_ips_list_password.append(password)
	m_ips_list.append(ip)


	#function calling
	entry_in_host_file(var_name,ip)
	copy_public_key(password,ip,var_name)
	group_ansible_hosts(ip)
f=open('../hosts','a')
f.write('[slaves]\n')
f.close()
for i in range(int(s_ips)):
	var_name='s'+str(i+1)
	password='s_p'+str(i+1)

	ip=data.getvalue(var_name)
	password=data.getvalue(password)
	s_ips_list_password.append(password)
	s_ips_list.append(ip)

	#function calling
	entry_in_host_file(var_name,ip)
	copy_public_key(password,ip,var_name)
	group_ansible_hosts(ip)
f=open('../hosts','a')
f.write('[clients]\n')
f.close()
for i in range(int(c_ips)):
	var_name='c'+str(i+1)
	password='c_p'+str(i+1)

	ip=data.getvalue(var_name)
	password=data.getvalue(password)
	c_ips_list_password.append(password)
	c_ips_list.append(ip)

	#function calling
	entry_in_host_file(var_name,ip)
	copy_public_key(password,ip,var_name)
	group_ansible_hosts(ip)

simple_setup_on_all_ips()
master_conf()
slave_conf()
client_conf()

print("It's Successfully created your cluster")
output= sp.getoutput('sudo sshpass -p {} ssh {} hadoop dfsadmin -report'.format(m_ips_list_password[0],m_ips_list[0]))
print(output)