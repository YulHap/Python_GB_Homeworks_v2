# Задача 5. Шифр Цезаря
# Юлий Цезарь использовал свой способ шифрования текста. Каждая буква
# заменялась на следующую по алфавиту через K позиций по кругу. Если взять
# русский алфавит и K, равное 3, то в слове, которое мы хотим зашифровать,
# буква А станет буквой Г, Б станет Д и так далее.
# Пользователь вводит сообщение и значение сдвига. Напишите программу,
# которая изменит фразу при помощи шифра Цезаря.
# Пример:
# Введите сообщение: это питон.
# Введите сдвиг: 3
# Зашифрованное сообщение: ахс тлхср.

# Решение 1 - без использования list comprehensions

txt = input('Введите сообщение: ')
k = int(input('Введите значение сдвига: '))

def сaesar_cipher(txt:str, shift:int) -> str:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    text_result = ''
    for symbol in txt:
        if symbol in alphabet:
            text_result = text_result + alphabet[(alphabet.index(symbol) + k) % len(alphabet)]
        else:
            text_result = text_result + symbol
    return text_result

print(сaesar_cipher(txt, k))

# Решение 2 - list comprehensions

txt = input('Введите сообщение: ')
k = int(input('Введите значение сдвига: '))
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

text_result = [alphabet[(alphabet.index(symbol) + k) % len(alphabet)] if symbol in alphabet else symbol for symbol in txt]

print(*text_result, sep ='')


# Решение 2.1 - list comprehensions. Решение 2 с методом join() в выводе

txt = input('Введите сообщение: ')
k = int(input('Введите значение сдвига: '))
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

text_result = [alphabet[(alphabet.index(symbol) + k) % len(alphabet)] if symbol in alphabet else symbol for symbol in txt]

print(''.join(text_result))
