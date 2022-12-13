# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента
# достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего
# конкурента?
# Делаем игру против бота
# а) Подумайте как наделить бота интеллектом

import random

count = 2021
person = random.randint(1, 2)
print('Играем против бота!')

while count != 0:
    if person == 1:
        print('Ходит игрок')
        write_value = int(input('Сколько конфет вы заберете? '))
        while write_value < 1 or write_value > 28 or write_value > count:
            if count > 28:
                write_value = int(input('Можно взять не больше 28 конфет! Сколько конфет вы заберете? '))
            else:
                write_value = int(input(f'Можно взять не больше {count} конфет! Сколько конфет вы заберете? '))
        count -= write_value
        person = 0
        print(f'Осталось {count} конфет!\n')
    else:
        print('Ходит бот')
        if count < 29:
            write_value = count
        elif count < 57:
            write_value = count - 29
        else:
            write_value = random.randint(1, 28)
        print(f'Бот взял конфет в количестве {write_value}')
        count -= write_value
        person = 1
        print(f'Осталось {count} конфет!\n')

if person == 0:
    print('Победил игрок!')
else:
    print('Победил бот!')