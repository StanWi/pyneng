# -*- coding: utf-8 -*-
'''
Задание 6.1b

Сделать копию скрипта задания 6.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip = input('Введите IP-адрес в формате 10.0.1.1: ').split('.')

while True:
    if len(ip) != 4:
        print('Incorrect IPv4 address')
    elif not ip[0].isdigit() or int(ip[0]) < 0 or int(ip[0]) > 255:
        print('Incorrect IPv4 address')
    elif not ip[1].isdigit() or int(ip[1]) < 0 or int(ip[1]) > 255:
        print('Incorrect IPv4 address')
    elif not ip[2].isdigit() or int(ip[2]) < 0 or int(ip[2]) > 255:
        print('Incorrect IPv4 address')
    elif not ip[3].isdigit() or int(ip[3]) < 0 or int(ip[3]) > 255:
        print('Incorrect IPv4 address')
    else:
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
        break
    ip = input('Введите IP-адрес в формате 10.0.1.1: ').split('.')
