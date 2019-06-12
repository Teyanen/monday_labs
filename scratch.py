print('введите строку')
a = input()

text = ''.join(reversed(a))
text = text.replace(')', ', ')
print(text.split('('))