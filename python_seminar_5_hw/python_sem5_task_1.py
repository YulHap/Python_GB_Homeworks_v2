# Задание 1. Поиск элемента
# Пользователь вводит искомый ключ. Если он хочет, то может ввести
# максимальную глубину — уровень, до которого будет просматриваться
# структура.
# Напишите функцию, которая находит заданный пользователем ключ в словаре
# и выдаёт значение этого ключа на экран. По умолчанию уровень не задан. В
# качестве примера можно использовать такой словарь:

# site = {
# 'html': {
# 'head': {
# 'title': 'Мой сайт'
# },
# 'body': {
# 'h2': 'Здесь будет мой заголовок',
# 'div': 'Тут, наверное, какой-то блок',
# 'p': 'А вот здесь новый абзац'
# }
# }
# }

# Пример 1
# Введите искомый ключ: head
# Хотите ввести максимальную глубину? Y/N: n
# Значение ключа: {'title': 'Мой сайт'}

# Пример 2
# Введите искомый ключ: head
# Хотите ввести максимальную глубину? Y/N: y
# Введите максимальную глубину: 1
# Значение ключа: None

site = {'html': {'head': {'title': 'Мой сайт'},
                 'body': {'h2': 'Здесь будет мой заголовок',
                          'div': 'Тут, наверное, какой-то блок',
                          'p': 'А вот здесь новый абзац'
                         }
                }
        }

result = None

def find_key(struct:dict, key:str, max_depth = None, depth = 1): # struct - словарь, в котором нужно искать ключ, key — искомый ключ, max_depth —максимальная глубина поиска, и depth — текущая глубина поиска
    global result
    if (not max_depth is None) and depth > max_depth:
        return result
    if key in struct:
        return struct[key]
    else:
        for _, value in struct.items():
            if isinstance(value, dict):
                result = find_key(value, key, max_depth, depth + 1)
        return result 

    
key = input('Введите искомый ключ: ')
answer = input("Хотите задать максимальную глубину? Y/N (Y - yes, N - no): ")
if answer.upper() == 'Y':
    given_depth = input('Задайте максимальную глубину: ') # given_depth - заданная глубина
    if given_depth.isdigit():
        given_depth = int(given_depth)
else:
    given_depth = None

result = find_key(site, key, given_depth, depth = 1)
print(result)
