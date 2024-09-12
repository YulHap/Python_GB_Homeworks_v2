# Задача 4. Уникальный шифр
# Напишите функцию, которая принимает строку и возвращает количество
# уникальных символов в строке. Используйте для выполнения задачи
# lambda-функции и map и/или filter.
# Сделайте так, чтобы алгоритм НЕ был регистрозависим: буквы разного
# регистра должны считаться одинаковыми.
# Пример:
# message = "Today is a beautiful day! The sun is shining and the birds are
# singing."
# unique_count = count_unique_characters(message)
# print("Количество уникальных символов в строке:", unique_count)
# Вывод: количество уникальных символов в строке — 5.



# Решение 1

from collections import Counter

message = "Today is a beautiful day! The sun is shining and the birds are singing."

def count_unique_characters(message:str) -> int:
    count_unic = list(filter(lambda v: v == 1, Counter(message.lower()).values()))
    return len(count_unic)

print(f'Количество уникальных символов в строке: {count_unique_characters(message)}')



# Решение 2 - без lambda-функций map, filter

from collections import Counter

message = "Today is a beautiful day! The sun is shining and the birds are singing."

def count_unique_characters(message:str) -> int:
    count_symbol = Counter(message.lower())
    count_unic = 0
    for k, v in count_symbol.items():
        if v == 1:
            count_unic += 1
    return count_unic

print(f'Количество уникальных символов в строке: {count_unique_characters(message)}')



# Решение 2.1 - решение 1 с генератором списка (list comprehension)

from collections import Counter

message = "Today is a beautiful day! The sun is shining and the birds are singing."

def count_unique_characters(message:str) -> int:
    count_symbol = Counter(message.lower())
    count_unic = len([value for key, value in count_symbol.items() if value == 1])
    return count_unic

print(f'Количество уникальных символов в строке: {count_unique_characters(message)}')