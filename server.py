#!/usr/bin/python3
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()

port = 9999

serversocket.bind((host, port))

serversocket.listen(5)

while True:
	clientsocket, addr = serversocket.accept()
	print ("Savienojums izveidots ar %s" % str(addr))
msg = 'Paldies par savienojumu'+ "\r\n"

clientsocket.send(msg.encode('ascii'))
clientsocket.close()




