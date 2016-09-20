#Python script to stop running services started by init during boot

import os
import sys
import subprocess

from array import *
	
if not os.geteuid() == 0:
	print "You need to be root to run this script"
	sys.exit(0)

print "Script running..."

initServices = ['apache2','bluetooth','cups','cups-browsed','dovecot','mongod','mysql','nginx','postfix','php5-fpm','ssh','smbd','tomcat','tor']

if len(sys.argv) < 2:
	print "Using default settings.."
	
	for i in initServices:
		print i
		subprocess.call(["initctl","stop",i])
