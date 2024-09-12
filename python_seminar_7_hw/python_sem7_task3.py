# Задача 3. Палиндром
# Используя модуль collections, реализуйте функцию can_be_poly, которая
# принимает на вход строку и проверяет, можно ли получить из неё палиндром.
# Пример кода:
# print(can_be_poly('abcba'))
# print(can_be_poly('abbbc'))
# Результат:
# True
# False


# Решение 1 - без collections

str1 = 'abcba'
str2 = 'abbbc'

def is_palindrom(string:str):
    i = 0
    j = len(string) - 1
    counter = 0
    iter = 0
    while i < j:
        iter += 1
        if string[i] == string[j]:
            counter += 1
        i += 1
        j -= 1
    if counter == int(len(string) / 2):
        return True
    else:
        return False

print(is_palindrom(str1))
print(is_palindrom(str2))

# Решение 2 - c collections

from collections import Counter


str1 = 'abcba'
str2 = 'abbbc'

def can_be_poly(string:str) -> bool:
    count = Counter(string)
    odd_symbols = len(list(filter(lambda x: x % 2 == 1, count.values())))
    return odd_symbols < 2

print(can_be_poly(str1))
print(can_be_poly(str2))

