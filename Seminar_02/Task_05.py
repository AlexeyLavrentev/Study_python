# Задача 5.	Реализуйте алгоритм перемешивания списка

import random

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list)
res = random.sample(list, len(list))
print(res)

