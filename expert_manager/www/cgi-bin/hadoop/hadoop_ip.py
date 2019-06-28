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
m_ips= data.getvalue('m_ips')
s_ips= data.getvalue('s_ips')
c_ips= data.getvalue('c_ips')

print("<form action='hadoop_ip_input.py'>")

print("""
<input type="hidden" name="m_ips" value={}>
<input type="hidden" name="s_ips" value={}>
<input type="hidden" name="c_ips" value={}>
""".format(m_ips,s_ips,c_ips))

for i in range(int(m_ips)):
	ip='m'+str(i+1)
	password='m_p'+str(i+1)
	print("""	
		<label>Enter master {} ip</label>
		<input type="text" name="{}"></br> 
		<label>Enter master {} password</label>
		<input type="text" name="{}"></br> 
		""".format(i+1,ip,i+1,password))


for i in range(int(s_ips)):
	ip='s'+str(i+1)
	password='s_p'+str(i+1)

	print("""	
		<label>Enter slave {} ip</label>
		<input type="text" name="{}"></br>
		<label>Enter slave {} password</label>
		<input type="text" name="{}"></br> 
		""".format(i+1,ip,i+1,password))

for i in range(int(c_ips)):
	ip='c'+str(i+1)
	password='c_p'+str(i+1)
	print("""	
		<label>Enter client {} ip</label>
		<input type="text" name="{}"></br> 
		<label>Enter client {} password</label>
		<input type="text" name="{}"></br> 
		""".format(i+1,ip,i+1,password))

print("<button>Send</button>")

print("</form>")


