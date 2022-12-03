#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import datetime

if __name__ == '__main__':
    # Список работников.
    pep = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о работнике.
            name = input("name faname? ")
            num = int(input("number? "))
            bday = list(map(int, input("Дата рождения: ").split('.')))
            br = datetime.date(bday[2], bday[1], bday[0])
        # Создать словарь.
            chel = {
                    'name': name,
                    'num': num,
                    'br': br,
            }

            # Добавить словарь в список.
            pep.append(chel)
            # Отсортировать список в случае необходимости.
            if len(pep) > 1:
                pep.sort(key=lambda item: item.get('br',''))

        elif command == 'list':
        # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                    "№",
                    "F.I.O.",
                    "NUMBER",
                    "BRDAY"
                )
            )
            print(line)

            # Вывести данные о всех сотрудниках.
            for idx, chel in enumerate(pep, 1):
               print(
                    f'| {idx:>4} |'
                    f' {chel.get("name", ""):<30} |'
                    f' {chel.get("num", 0):<15} |'
                    f' {chel.get("br")}      |'
               )
                

            print(line)

        elif command == 'select':
            
            # Получить требуемый стаж.
            zapros = int(input("zapros po numeru  "))

            # Инициализировать счетчик.
            count = 0
            # Проверить сведения работников из списка.
            for chel in pep:
                if chel.get('num') == zapros:
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, chel.get('name', ''))
                    )

            # Если счетчик равен 0, то работники не найдены.
            if count == 0:
                print("cheela s takim nomerom net")
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - add chel;")
            print("list - show list of pep;")
            print("select <стаж> - запросить работников со стажем;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


