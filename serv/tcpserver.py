import socket
import sys
import time

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
print("")
print("Sever adress is", host)
print("")
name = input(str("Ievadiet lietotajvardu: "))
s.listen(1)
print("")
print("Sagaidam ienakosos savienojumus ... ")
print("")
conn, addr = s.accept()
print("Sanemts savienojuma pieprasijums")

#connection done ###

s_name = conn.recv(1024)
s_name = s_name.decode()
print("")
print(s_name, "ir pievienojies sarakstei")
print("")
conn.send(name.encode())

## messaging loop ##

while 1:
    message = input(str("Ievadiet zinojumu: "))
    print("")
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print("")
    print(name,": ",message)
    print("")
