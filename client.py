import socket


c = ('localhost', 550)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(c)

data = client.recv(1024)
print(data)