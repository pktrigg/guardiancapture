#!/usr/bin/python3
#name:		  UDPServer
#created:	   August 2018
#by:			paul.kennedy@guardiangeomatics.com
#description:   python module to read UDP ports
#notes:

# See readme.md for more details

import socket
import socket
# import fcntl
import struct


def get_ip_address(name):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
# def get_ip_address2(ifname):

# 	socket.gethostbyname(socket.gethostname())

# 	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 	try:
# 		return socket.inet_ntoa(fcntl.ioctl(
# 			s.fileno(),
# 			0x8915,  # SIOCGIFADDR
# 			struct.pack('256s', bytes(ifname[:15], 'utf-8'))
# 			)[20:24])
# 	except:
# 		return ('localhost')

# Here we define the UDP IP address as well as the port number that we have 
# already defined in the client python script.

def main():
	'''UDP SERVER receives data from a client and does something with it (typically capture to disc)'''
	UDP_PORT_NO = 5019
	print ("Listening on UDP Port: %d" %(UDP_PORT_NO))
	eth0 = get_ip_address('eth0')
	print ("Ethernet IP: %s will be used as priority" % (eth0))
	if eth0 is 'localhost':
		wlan0 = get_ip_address('wlan0')
		UDP_IP_ADDRESS = wlan0
		print ("WiFi IP:", wlan0)
	else:	
		UDP_IP_ADDRESS = eth0

	print ("Listening on IP:", UDP_IP_ADDRESS)

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



###############################################################################################
if __name__ == "__main__":
	main()
	# exit()
