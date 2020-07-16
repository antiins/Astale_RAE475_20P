import socket
import sys
import time

print("Laipni aicinati")
print("")
print("Initiallsing....")
time.sleep(1)

s = socket.socket()
print("")
host = input(str("Ievadiet servera adresi : "))
print("")
name = input(str("Ievadiet savu lietotajvardu : "))
port = 8080
print("")
time.sleep(1)
s.connect((host,port))
print("Savienots...")

## Conection done ##

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print("")
print( s_name, "pievienojies sarakstei ")

while 1:
    message = s.recv(1024)
    message = message.decode()
    print("")
    print(name,": ",message)
    print("")
    message = input(str("Ievadiet savu zinojumu : "))
    print("")
    s.send(message.encode())
