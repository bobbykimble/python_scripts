ipadd = raw_input('enter ip address:')
username = raw_input('enter username:')
password = raw_input('enter password:')
import paramiko
import os
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ipadd, username=username, password=password)
import os
stdin, stdout, stderr = ssh.exec_command('ls -l /etc')
fobj = open('fileout.txt', 'w') 
fobj.write(stdout.read())
fobj.close()
ssh.close()
