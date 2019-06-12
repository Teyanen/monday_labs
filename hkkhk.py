path1 = "C:/Users/Андрей/PycharmProjects/123/monday.txt"
path2 = 'C:/Users/Андрей/PycharmProjects/123/thsd.txt'
path3 = 'C:/Users/Андрей/PycharmProjects/123/wnds.txt'
path4 = 'C:/Users/Андрей/PycharmProjects/123/trsd.txt'
path5 = 'C:/Users/Андрей/PycharmProjects/123/frd.txt'
path6 = "C:/Users/Андрей/PycharmProjects/123/monday2.txt"
path7 = 'C:/Users/Андрей/PycharmProjects/123/thsd2.txt'
path8 = 'C:/Users/Андрей/PycharmProjects/123/wnds2.txt'
path9 = 'C:/Users/Андрей/PycharmProjects/123/trsd2.txt'
path10 = 'C:/Users/Андрей/PycharmProjects/123/frd2.txt'

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

print("При запросе верхней недели введите 1, при запросе нижней 2")

b = input()
b = int(b)

if b<1 or b>2:
    print("Неверное число")

print("Введите день недели от 1 до 7")

a = input()
a = int(a)


if a == 1 and b == 1:
    print(monday_file.read())

if a == 2 and b == 1:
    print(thsd_file.read())

if a == 3 and b == 1:
    print(wnds_file.read())

if a == 4 and b == 1:
    print(trsd_file.read())

if a == 5 and b == 1:
    print(frd_file.read())

if a == 1 and b == 2:
    print(monday2_file.read())

if a == 2 and b == 2:
    print(thsd2_file.read())

if a == 3 and b == 2:
    print(wnds2_file.read())

if a == 4 and b == 2:
    print(trsd2_file.read())

if a == 5 and b == 2:
    print(frd2_file.read())

if a == 6 or a == 7:
    print("Пар нет")

if a > 7 or a < 1:
    print("Неверное число")