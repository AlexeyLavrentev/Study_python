# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = input("\nВведите вещественное число: ")

sum_digit = 0
for char in number:
    if char.isdigit():
        sum_digit += int(char)

print("\n  Сумма цифр введённого числа =", sum_digit)