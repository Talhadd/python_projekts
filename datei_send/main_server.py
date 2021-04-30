import os
import socket

host = "0.0.0.0"
sep = "$$SEP$$"
port = 1331
buf = 1024
s = socket.socket()

s.bind((host, port))
s.listen(5)
print("bereit...")

client_socket, adress = s.accept()
print(f"{adress}hat sich verbunden")

File, file_size = client_socket.recv(buf).split(sep)
file_size = int(file_size)
with open(file, "wb") as f:
    bytes_recv = client_socket.recv(buf)    
    while bytes_recv:
        f.write(bytes_recv)
        bytes_recv = client_socket.recv(buf)
       