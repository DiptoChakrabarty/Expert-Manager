import os
import subprocess
import getpass
def local_webserver():
	os.system("echo '[web]' | cat > hosts")
	os.system("echo '127.0.0.1 ansible_user=root ansible_password=redhat' | cat >> hosts")
	os.system("ansible-playbook playbooks/webserver.yml")

def remote_webserver(ip,username,password):
	import os
	
	os.system("echo '[web]' | cat > hosts")
	
	os.system("sshpass -p {} ssh-copy-id {}@{}".format(password,username,ip))
	os.system("echo '{} ansible_user={} ansible_password={}' | cat >> hosts".format(ip,username,password))
	
	os.system("ansible-playbook playbooks/webserver.yml")

def local_docker(docker_no,docker_name):
	os.system("echo '[docker]' | cat > hosts")
	os.system("echo '127.0.0.1 ansible_user=root ansible_password=redhat' | cat >> hosts")
	

	for i in range(int(docker_no)):
		os.system("echo 'docker_name: {}' | cat > playbooks/data.yml".format(docker_name[i]))
		os.system("ansible-playbook playbooks/launch_container.yml")

def remote_docker(docker_no,docker_name,ip,username,password):
	os.system("echo '[docker]' | cat > hosts")
	os.system("sshpass -p {} ssh-copy-id {}@{}".format(password,username,ip))
	os.system("echo '{} ansible_user={} ansible_password={}' | cat >> hosts".format(ip,username,password))
	

	for i in range(int(docker_no)):
		os.system("echo 'docker_name: {}' | cat > playbooks/data.yml".format(docker_name[i]))
		os.system("ansible-playbook playbooks/remote_docker.yml")

def mail(mail_id_sender,password,mail_id_receiver,subject,body):
	os.system("echo 'mail_id_sender: {}' | cat  > playbooks/data.yml".format(mail_id_sender))
	os.system("echo 'password: {}' | cat  >> playbooks/data.yml".format(password))
	os.system("echo 'mail_id_receiver: {}' | cat  >> playbooks/data.yml".format(mail_id_receiver))
	os.system("echo 'subject: {}' | cat  >> playbooks/data.yml".format(subject))
	os.system("echo 'body : {}' | cat  >> playbooks/data.yml".format(body))

	os.system("ansible-playbook playbooks/mail.yml ")


def sms(number,msg):
	os.system("echo 'number: {}' | cat  > playbooks/data.yml".format(number))
	os.system("echo 'msg: {}' | cat  >> playbooks/data.yml".format(msg))
	os.system("ansible-playbook playbooks/message.yml")


def yum():
	ip_no=input("Enter no of ip's where you want to perform this task")
	os.system("echo '[yum]' | cat > hosts")
	for i in range(int(ip_no)):
		ip=input("Enter ip of remote")
		username=input("Enter username with whom you want to be performed this task")
		password=input("Enter password of given user")
		os.system("sshpass -p {} ssh-copy-id {}@{}".format(password,username,ip))
		os.system("echo '{} ansible_user={} ansible_password={}' | cat >> hosts".format(ip,username,password))
	os.system("ansible-playbook playbooks/yum.yml")