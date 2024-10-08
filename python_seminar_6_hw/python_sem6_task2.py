# Задача 2. Случайные соревнования
# Мы хотим протестировать работу электронной таблицы для участников
# некоторых соревнований. Есть два списка, то есть две команды, по 20
# участников в каждом. В них хранятся очки каждого участника — вещественные
# числа с двумя знаками после точки, например 4.03.
# Член одной команды соревнуется с участником другой команды под таким же
# номером. То есть первый соревнуется с первым, второй — со вторым и так
# далее.
# Напишите программу, которая генерирует два списка участников (по 20
# элементов) из случайных вещественных чисел (от 5 до 10). Для этого найдите
# подходящую функцию из модуля random. Затем сгенерируйте третий список, в
# котором окажутся только победители из каждой пары.
# Пример:
# Первая команда: [7.86, 6.76, 9.97, 9.08, 5.45, 6.9, 8.65, 5.17, 8.17, 5.06, 7.56, 7.1,
# 7.18, 8.25, 5.53, 7.95, 8.91, 7.11, 8.29, 9.52]
# Вторая команда: [7.13, 5.7, 8.89, 5.36, 5.62, 9.46, 5.82, 8.67, 8.41, 7.0, 5.31, 7.8,
# 9.93, 7.76, 7.4, 8.26, 7.94, 5.71, 7.89, 7.77]
# Победители тура: [7.86, 6.76, 9.97, 9.08, 5.62, 9.46, 8.65, 8.67, 8.41, 7.0, 7.56, 7.8,
# 9.93, 8.25, 7.4, 8.26, 8.91, 7.11, 8.29, 9.52]


# Решение 1 - функции, циклы

import random

comand = []

def ball_random(comand: list, start, end, count:int) -> list:
    comand = []
    for i in range(count):
        comand.append(round((random.uniform(start, end)), 2))
    return comand


def winner_list(list1:list, list2:list) -> list:
    winner = []
    if len(list1) == len(list2):
        for i in range(len(list1)):
            winner.append(max(list1[i], list2[i]))
    else:
        print('Длина списков должна быть одинаковой!')
    return winner

comand1 = ball_random(comand, 5, 10, 20)
comand2 = ball_random(comand, 5, 10, 20)
winners = winner_list(comand1, comand2)

print(f'Первая команда: {comand1}')
print(f'Вторая команда: {comand2}')
print(f'Победители тура: {winners}')

# Решение 2 - с генератором списка (list comprehension)

import random

comand1 = [round((random.uniform(5, 10)), 2) for _ in range(20)]
comand2 = [round((random.uniform(5, 10)), 2) for _ in range(20)]
winners = [max(comand1[i], comand2[i]) if len(comand1) == len(comand2) else None for i in range(len(comand1))]

print(f'Первая команда: {comand1}', f'Вторая команда: {comand2}', f'Победители тура: {winners}', sep = '\n')
