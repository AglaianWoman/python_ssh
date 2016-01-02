import paramiko
#using paramiko a python module for remote connection
ssh = paramiko.SSHClient()

# replace XX with relevant data



try:	
#Adding policy
	ssh.set_missing_host_key_policy(
	    paramiko.AutoAddPolicy())
# establishing connection

#	ssh.connect('ip_address'),username='username', password='password',port=port_no)
	ssh.connect('XX.XX.XX.XX', username='XX.XX.XX.XX', password='XX.XX.XX.XX', port=XX)
except:
	print ("Unable to establish connection")

stdin, stdout, stderr=ssh.exec_command("ls ") #executing commands
#displaying the commands executed
print(stdout.read())

