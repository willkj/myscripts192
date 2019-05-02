#/usr/bin/python
import socket, sys
from time import sleep
ip = input('IP: ')
sleep(3)
print("Starting...")
for port in range(1, 65535):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if s.connect_ex((ip, port)) == 0:
		print ("port {} [OPENED]".format(port))
		s.close()
