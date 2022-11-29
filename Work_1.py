# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
#
# import random
#
# some_list = []
# sum = 0
# for i in range(int(input('Введите колличество элементов в списке: '))):
#     some_list.append(random.randint(0, 9))
#     if i % 2 == 1:
#         sum += some_list[i]
#
# print(f'Список: {some_list}')
# print(f'Сумма нечетных элементов: {sum}')


###########################################################################
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
#
# import random
#
# some_list = []
# for i in range(int(input('Введите колличество элементов в списке: '))):
#     some_list.append(random.randint(0, 9))
# print(f'Искомый список: {some_list}')
#
# some_list2 = []
# temp = 0
# for i in range(int(len(some_list) / 2 + 1)):
#     if len(some_list) % 2 != 0 or int(len(some_list) / 2) > i:
#         some_list2.append(some_list[i] * some_list[-i - 1])
# print(f'Новый список: {some_list2}')


#######################################################################################
# Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
#
# import random
#
# some_list = []
# for i in range(int(input('Введите колличество элементов в списке: '))):
#     some_list.append(round(random.random() * 10, 2))
# print(f'Искомый список: {some_list}')
# print(f'Разница между Max и Min значениями: {max(some_list) - min(some_list)}')



# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
#
# N = int(input('Введите целое десятичное число: '))
# bin_num = bin(N)
# print(f'{N} -> {bin_num[2:]}')



# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#
# N = int(input('Введите целое число: '))
#
# fib1 = 1
# fib2 = 1
# some_list = []
# some_list.extend([fib1, fib2])
#
# for _ in range(2, N):
#     fib1, fib2 = fib2, fib1 + fib2
#     some_list.append(fib2)
#
# print(f'Список Фибоначчи: {some_list}')
#
# some_list2 = []
# for i in range(len(some_list)):
#     some_list2.append(-(some_list[-1-i]))
# some_list2.append(0)
# some_list2.extend(some_list)
#
# print(f'Список Фибоначчи с отрицательными индексами: {some_list2}')
