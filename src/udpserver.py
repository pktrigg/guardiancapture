#name:		  UDPServer
#created:	   August 2018
#by:			paul.kennedy@guardiangeomatics.com
#description:   python module to read UDP ports
#notes:

# See readme.md for more details

import socket

# Here we define the UDP IP address as well as the port number that we have 
# already defined in the client python script.

UDP_IP_ADDRESS = "192.168.15.87"
UDP_PORT_NO = 5019
# Once we''ve imported the socket module and declared our ip address and port number we can create another socket which will look exactly like the socket we constructed in our client program.

# declare our serverSocket upon which
# we will be listening for UDP messages
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# One difference is that we will have to bind our declared IP address
# and port number to our newly declared serverSock
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
# And finally, once we've created our server socket, we need to write the code that will keep our script continuously listening to this socket until its termination. This takes form as a simple while loop, like so:

while True:
	data, addr = serverSock.recvfrom(1024)
	print ("Message: ", data)