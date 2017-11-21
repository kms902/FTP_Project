# Client
# Kevin Singleton
# cd, dir, get, put, mget, mput, quit
import os
import socket

IP = "169.254.240.223"    
PORT = 21            
#socket.settimeout(3)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
message = input()
s.sendall(message.encode())
data = s.recv(1024)
print('Received :', repr(data.decode()))
