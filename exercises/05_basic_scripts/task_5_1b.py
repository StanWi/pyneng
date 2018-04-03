# -*- coding: utf-8 -*-
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

ip_mask = argv[1]
tmp = ip_mask.split('/')
ip = [int(i) for i in tmp[0].split('.')]
nmask = int(tmp[1])
mask = ''
for i in range(32):
    if i < nmask:
        mask += '1'
    else:
        mask += '0'
m = [int(mask[8*i:8*(i+1)], 2) for i in range(4)]

ip_bit = '{:08b}{:08b}{:08b}{:08b}'.format(ip[0], ip[1], ip[2], ip[3])
ip_net_bit = ip_bit[0:nmask] + mask[nmask:32]
ip = [int(ip_net_bit[8*i:8*(i+1)], 2) for i in range(4)]


template = '''
Network:
{i0:<8} {i1:<8} {i2:<8} {i3:<8}
{i0:08b} {i1:08b} {i2:08b} {i3:08b}

Mask:
/{m}
{m0:<8} {m1:<8} {m2:<8} {m3:<8}
{m0:08b} {m1:08b} {m2:08b} {m3:08b}
'''
print(template.format(i0=ip[0],i1=ip[1],i2=ip[2],i3=ip[3],
                      m=nmask,m0=m[0],m1=m[1],m2=m[2],m3=m[3]))
