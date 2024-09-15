# Задача 4. Частотный анализ
# Есть файл text.txt, который содержит текст. Напишите программу, которая
# выполняет частотный анализ, определяя долю каждой буквы английского
# алфавита в общем количестве английских букв в тексте, и выводит результат в
# файл analysis.txt. Символы, не являющиеся буквами английского алфавита,
# учитывать не нужно.
# В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте, с
# тремя знаками в дробной части. Буквы должны быть отсортированы по
# убыванию их доли. Буквы с равной долей должны следовать в алфавитном
# порядке.
# Пример:
# Содержимое файла text.txt:
# Mama myla ramu.
# Содержимое файла analysis.txt:
# a 0.333
# m 0.333
# l 0.083
# r 0.083
# u 0.083
# y 0.083

eng_alph = 'abcdefghijklmnopqrstuvwxyz'

with open("python_seminar_8_hw/file_for_hw8/text.txt", "r", encoding="utf-8") as text:
    txt = text.read().lower() # mama myla ramu.
    letter_list = [let for let in txt if let in eng_alph] # ['m', 'a', 'm', 'a', 'm', 'y', 'l', 'a', 'r', 'a', 'm', 'u'] - 12 символов
    letter_set = sorted(set([let for let in txt if let in eng_alph])) # ['a', 'l', 'm', 'r', 'u', 'y']
    let_count = {} # {'a': 0.333, 'l': 0.083, 'm': 0.333, 'r': 0.083, 'u': 0.083, 'y': 0.083}
    for i in letter_set: 
        count = 0
        for n in letter_list:
            if n == i:
                count += 1
                let_count[i] = round((count / len(letter_list)), 3)
    sorted_let_count = sorted(let_count.items(), key=lambda item: item[1], reverse=True) 
    # sorted_let_count = [('a', 0.333), ('m', 0.333), ('l', 0.083), ('r', 0.083), ('u', 0.083), ('y', 0.083)]

with open("python_seminar_8_hw/file_for_hw8/analysis.txt", "w", encoding="utf-8") as an:
    for i in sorted_let_count:
        print(*i, file = an)


    





