# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def func_list(n_list):
    mult = []
    for i in range(len(n_list) // 2):
        mult.append(n_list[i] * n_list[-1 -i])
    if len(n_list)%2 != 0:
        mult.append((n_list[len(n_list) // 2])**2)
    return mult


list_01 = [5, 7, 2, 9, 3, 8, 4, 1, 6, 3, 7]

mult_01 = func_list(list_01)

print("Произведение пар чисел третьего списка: ", mult_01)