# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

num = int(input("\nВведите число: "))

result = []
sum = 0
for i in range(1, num+1):
    res = round((1 + 1/i)**i, 3)
    sum += res
    result.append(res)

print(result)
print("   Сумма чисел последовательности: ", round(sum, 3))