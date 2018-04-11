# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию скрипта задания 9.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(config):
    access = {}
    trunk = {}
    with open(config) as f:
        interface = ''
        for line in f:
            if line.startswith('interface'):
                if interface:
                    access[interface] = 1
                interface = line.split()[1]
            elif line.lstrip().startswith('switchport access vlan'):
                access[interface] = line.split()[3]
                interface = ''
            elif line.lstrip().startswith('switchport trunk allowed vlan'):
                trunk[interface] = line.split()[4].split(',')
                interface = ''
    return access, trunk

access, trunk = get_int_vlan_map('config_sw2.txt')
print(access)
print(trunk)
