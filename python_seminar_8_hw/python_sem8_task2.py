# Задание 2. Сумма чисел
# В файле zen.txt хранится так называемый Дзен Пайтона — текст философии
# программирования на языке Python. Выглядит он так:
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
# Напишите программу, которая выводит на экран все строки этого файла в
# обратном порядке

with open("file_for_hw8/zen.txt", encoding="utf-8") as file:
    txt = file.readlines()

for line in reversed(txt):
    print(line, end='')

# FileNotFoundError: [Errno 2] No such file or directory: 'file_for_hw8/zen.txt'