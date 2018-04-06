# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
mac = []
with open('CAM_table.txt') as f:
    for line in f:
        if 'DYNAMIC' in line:
            mac.append(line.replace('  DYNAMIC    ','').strip())
for line in sorted(mac):
    print(line)
