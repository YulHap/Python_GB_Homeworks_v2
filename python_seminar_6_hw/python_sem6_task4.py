# Задача 4. Список списков
# Дан многомерный список:
# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# Напишите код, который раскрывает все вложенные списки, то есть оставляет
# лишь внешний список. Для решения используйте только list comprehensions.
# Ответ: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

# Решение 1 - list comprehensions

nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

list_res = [el 
            for el_list in nice_list 
            for el_list1 in el_list 
            for el in el_list1]

print(list_res)

# Решение 2 - рекурсия без list comprehensions

nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

def output_list(list1:list) -> list:
    list_res = []
    for i in list1:
        if type(i) is int:
            list_res.append(i)
        elif type(i) is list:
            list_res.extend(output_list(i))
    return list_res

print(output_list(nice_list))