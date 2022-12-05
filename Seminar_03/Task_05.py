# Задача 5.	Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

num = int(input("Введите число: "))

def fib(n):
    fib_nums = []
    a, b = 1, 1
    for i in range(n):
        fib_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(n+1):
        fib_nums.insert(0, a)
        a, b = b, a - b
    return fib_nums

print(fib(num))