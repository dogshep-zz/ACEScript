#!/usr/bin/python

# imports
import getpass
import os
import subprocess

# check for sudo
if os.geteuid() != 0:
	exit("You need to have root privileges to run this script.\nPlease try again")
print('Openconnect connection to Cisco AnyConnect')

# get inputs
host = raw_input('Connect to: ')
user = raw_input('Username: ')

# add strings together
connection = 'openconnect -u %s %s' % (user, host)

# display connecting host
print('Connecting to %s' % host)

# connect
os.system(connection)

