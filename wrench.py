#!/usr/bin/env python2
# wrench.py
# socket things!
# socket things at http://docs.python.org/2/howto/sockets.html
from sys import argv
import socket

script, string = argv

print "The script is called %s and the string to echo is %s\n" %(script, string)

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host
serversocket.bind((socket.gethostname(), 80))
# become a server socket
serversocket.listen(5)
