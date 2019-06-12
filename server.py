import socket
path1 = "monday.txt"
path2 = 'thsd.txt'
path3 = 'wnds.txt'
path4 = 'trsd.txt'
path5 = 'frd.txt'
path6 = "monday2.txt"
path7 = 'thsd2.txt'
path8 = 'wnds2.txt'
path9 = 'trsd2.txt'
path10 = 'frd2.txt'
monday_file = open(path1, "r")
thsd_file = open(path2, "r")
wnds_file = open(path3, "r")
trsd_file = open(path4, "r")
frd_file = open(path5, "r")
monday2_file = open(path6, "r")
thsd2_file = open(path7, "r")
wnds2_file = open(path8, "r")
trsd2_file = open(path9, "r")
frd2_file = open(path10, "r")

sock = socket.socket()
sock.bind(('',1000))
sock.listen(1)
print('Подключение пользователя...')
conn, adr = sock.accept()
print('Подключен пользователь с ip: '+str(adr))
t = 'При запросе верхней недели введите 1, при запросе нижней 2'
conn.send(t.encode())

b = int(conn.recv(1))

if b<1 or b>2:
    t = "Неверное число"
    conn.send(t.encode())

t = "Введите день недели от 1 до 7"
conn.send(t.encode())

a = int(conn.recv(1))

if a == 1 and b == 1:
    conn.send(monday_file.read().encode())

if a == 2 and b == 1:
    conn.send(thsd_file.read().encode())

if a == 3 and b == 1:
    conn.send(wnds_file.read().encode())

if a == 4 and b == 1:
    conn.send(trsd_file.read().encode())

if a == 5 and b == 1:
    conn.send(frd_file.read().encode())

if a == 1 and b == 2:
    conn.send(monday2_file.read().encode())

if a == 2 and b == 2:
    conn.send(thsd2_file.read().encode())

if a == 3 and b == 2:
    conn.send(wnds2_file.read().encode())

if a == 4 and b == 2:
    conn.send(trsd2_file.read().encode())

if a == 5 and b == 2:
    conn.send(frd2_file.read().encode())

if a == 6 or a == 7:
    t = "Пар нет"
    conn.send(t.encode())

if a > 7 or a < 1:
    t = "Неверное число"
    conn.send(t.encode())
