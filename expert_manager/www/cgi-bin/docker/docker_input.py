#!/usr/bin/python36

import subprocess as sp
import cgi
import os
print("content-type: text/html")
print()
	
print("""
<form action='docker_container.py'>
<label>Enter docker name would you want to launch</label></br>
<input type='text' name='docker_name'></br>
<button>Submit</button>
</form>""")