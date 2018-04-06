# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
vlan = input('Введите номер VLAN: ')
mac = []
with open('CAM_table.txt') as f:
    for line in f:
        if 'DYNAMIC' in line:
            mac.append(line.replace('  DYNAMIC    ','').strip())
for line in sorted(mac):
    if vlan in line:
        print(line)
