# Задача 3. Измените код одной-двух решенных ранее задач
# (с прошлых семинаров или домашних работ), применив лямбды,
# filter, map, zip, enumerate, списочные выражения.

# прошлое решение задачи 3 семинара 3

# list_01 = [1.5, 2.2, 5.1, 5, 7.6]
#
# new_list = []
# for i in range(len(list_01)):
#     temp = round((list_01[i] - int(list_01[i])), 2)
#     if temp != 0:
#         new_list.append(temp)
#
# print("Разница между максимальным и минимальным: ", max(new_list) - min(new_list))

# новое решение

list_01 = [1.5, 2.2, 5.1, 5, 7.6]
new_list = [round((x - int(x)), 2) for x in list_01 if ((x - int(x))) != 0]
print(new_list)
print("Разница между максимальным и минимальным: ", max(new_list) - min(new_list))