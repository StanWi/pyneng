# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

file = argv[1]

with open(file) as f, open('config_sw1_cleared.txt', 'w') as w:
    for line in f:
        for phrase in ignore:
            if phrase in line:
                break
        else:
            w.write(line)
