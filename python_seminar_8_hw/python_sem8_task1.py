# Задание 1. Сумма чисел
# Во входном файле numbers.txt записано N целых чисел, которые могут быть
# разделены пробелами и концами строк. Напишите программу, которая выводит
# сумму чисел во выходной файл answer.txt.
# Пример:
# Содержимое файла numbers.txt
#      2       
# 2       
#       2
#  2      
# Содержимое файла answer.txt
# 8

with open('python_seminar_8_hw/file_for_hw8/numbers.txt', 'r', encoding='utf-8') as file1:
    res = 0
    for line in file1:
        string = [int(sym) for sym in line if sym.isdigit()]
        res += sum(string)

with open('python_seminar_8_hw/file_for_hw8/answer.txt', 'a', encoding='utf-8') as file2:
    print(res, file = file2)

