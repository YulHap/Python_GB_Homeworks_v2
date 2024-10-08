# Задание 1. Гласные буквы
# Команде лингвистов понравилось качество ваших программ, поэтому они
# решили заказать функцию для анализатора текста, которая создавала бы
# список гласных букв в нём и считала бы их количество.
# Напишите программу, которая запрашивает у пользователя текст и генерирует
# список гласных букв этого материала (сама строка вводится на русском языке).
# Выведите в консоль сам список и его длину.
# Пример:
# Введите текст: Нужно отнести кольцо в Мордор!
# Список гласных букв: ['у', 'о', 'о', 'е', 'и', 'о', 'о', 'о', 'о']
# Длина списка: 9

# Решение 1 - с циклом

vowels_rus = 'ауоыиэяюёе'

txt = input('Введите текст: ')
vowels_txt = []
vowels_count = 0

for let in txt:
    if let in vowels_rus:
        vowels_txt.append(let)
        vowels_count += 1

print(f'Список гласных букв: {vowels_txt}')
print(f'Длина списка: {vowels_count}')


# Решение 2 - с генератором списка (list comprehension)

txt = input('Введите текст: ')
vowels_txt = [let for let in txt if let in 'ауоыиэяюёе']

print(f'Список гласных букв: {vowels_txt}')
print(f'Длина списка: {len(vowels_txt)}')
