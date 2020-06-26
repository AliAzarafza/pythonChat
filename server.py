import socket

inf = ('localhost', 550)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(inf)

server.listen(20)
con ,addr = server.accept()

while True:
    sendData = raw_input(">> ")
    con.send(sendData)