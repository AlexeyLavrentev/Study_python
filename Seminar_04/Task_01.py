# Вычислить число c заданной точностью d

from math import pi
from decimal import*
d =  Decimal(input("Введите точность для числа π: "))
print(f'число Пи с заданной точностью {d} равно {str(pi)[:len(str(d))]}')