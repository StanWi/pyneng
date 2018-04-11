# -*- coding: utf-8 -*-
'''
Задание 9.4a

Задача такая же, как и задании 9.4.
Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл.
В нем есть разделы с большей вложенностью, например, разделы:
* interface Ethernet0/3.100
* router bgp 100

Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности.
При этом, не привязываясь к конкретным разделам.
Она должна быть универсальной, и сработать, если это будут другие разделы.

Если уровня вложенности два:
* то команды верхнего уровня будут ключами словаря,
* а команды подуровней - списками

Если уровня вложенности три:
* самый вложенный уровень должен быть списком,
* а остальные - словарями.

На примере interface Ethernet0/3.100:

{'interface Ethernet0/3.100':{
               'encapsulation dot1Q 100':[],
               'xconnect 10.2.2.2 12100 encapsulation mpls':
                   ['backup peer 10.4.4.4 14100',
                    'backup delay 1 1']}}


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']


def check_ignore(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет

    '''
    return any(word in command for word in ignore)

def switch_config(file):
    config = {}
    level2 = []
    level3 = []
    with open(file) as f:
        commands = f.read().rstrip().split('\n')
        for command in commands[::-1]:
            if not check_ignore(command, ignore) and not command.startswith('!') and command.strip() != '':
                if command.startswith(2 * ' '):
                    level3.append(command)
                elif command.startswith(' ') and len(level3) > 0:
                    level2 = {}
                    level2[command] = level3[::-1]
                    level3 = []
                elif command.startswith(' ') and len(level2) > 0 and level2.isdict():
                    level2[command] = []
                elif command.startswith(' ') and len(level2) == 0:
                    level2 = []
                    level2.append(command)
                elif not command.startswith(' ') and len(level2) > 0:
                    config[command] = level2
                    level2 = []
    return config

print(switch_config('config_r1.txt'))
