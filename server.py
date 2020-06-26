import socket

inf = ('host ip', 550)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(inf)

server.listen(20)
con ,addr = server.accept()

con.send("hello")