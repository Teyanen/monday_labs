import socket
conn = socket.socket()
ad = input('IP адрес сервера: ')
conn.connect((ad,1000))
b = input(conn.recv(128).decode() + ' ')
conn.send(b.encode())
a = input(conn.recv(128).decode() + ' ')
conn.send(a.encode())
print(conn.recv(100).decode())
