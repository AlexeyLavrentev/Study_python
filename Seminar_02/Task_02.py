# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

number = int(input("\nВведите число: "))

result = []
for i in range(1, number+1):
    res = 1
    for j in range(1, i+1):
        res *= j
    result.append(res)

print("\n  Набор произведений чисел от 1 до N: ")
print(" ", result)