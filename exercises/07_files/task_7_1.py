# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

template = """
Protocol:              {}
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface:    {}
"""
protocol = {'O':'OSPF'}

with open('ospf.txt') as f:
    for line in f:
        ospf = line.split()
        print(template.format(protocol[ospf[0]],ospf[1],ospf[2].strip('[]'),ospf[4].strip(','),ospf[5].strip(','),ospf[6]))
