import socket
import os

host = "192.168.178.100"
port = 1331

sep = "$$SEP$$"
File = r"file name"
buf = 1024
file_size = os.path.getsize(File)
s = socket.socket()

if sep in File:
    print("Nimm ein anderen Namen für die datei")
    exit(-1)

file_size = os.path.getsize(File)

s.connect((host, port))
s.send(f"{File}{sep}{file_size}".encode())


with open(File, 'rb') as f: 
    while True:
        file_bytes = f.read(buf)
        if not file_bytes: 
            break
        s.sendall(file_bytes)