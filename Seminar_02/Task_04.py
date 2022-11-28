# Задача 4.	Задайте числами список из N элементов, заполненных из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.

from random import randint
N = int(input('Введите число N: '))
if N <=0:
    print('Введите другое число')
else:
    numbers = [randint(-N, N) for i in range(2*N+1)]
    print('Список', numbers)
    index = int(input('Произведение какого количество чисел вы хотите увидеть: '))
    calc = 1
    for i in range(index):
        ind = int(input('Введите номер позиции: '))
        calc = calc*numbers[ind]
    print('Произведение элементов: ', calc)
