# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ip = input('Введите IP-адрес в формате 10.0.1.1: ').split('.')
correct = True

if len(ip) != 4:
    correct = False

for i in ip:
    if not i.isdigit() or int(i) < 0 or int(i) > 256:
        correct = False
        break

if correct:
    if int(ip[0]) > 0 and int(ip[0]) < 224:
        print('unicast')
    elif int(ip[0]) > 0 and int(ip[0]) < 240:
        print('multicast')
    elif '.'.join(ip) == '255.255.255.255':
        print('local broadcast')
    elif '.'.join(ip) == '0.0.0.0':
        print('unassigned')
    else:
        print('unused')
else:
    print('Incorrect IPv4 address')
