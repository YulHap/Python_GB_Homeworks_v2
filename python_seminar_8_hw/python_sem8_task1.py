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



# numbers_txt = open("file_for_hw8/numbers.txt", encoding="utf-8")
# print(numbers_txt.read())
# res = 0 

# for string in numbers_txt :
#     numbers = [int(i) for i in string.split()]
#     res += sum(numbers)
# numbers_txt.close()


# sum_file = open("answer.txt", "w", encoding="utf-8") 
# sum_file.write(str(res))
# sum_file.close()


# with open("file_for_hw8\numbers.txt", 'r', encoding="utf-8") as file:
#     s = file.readlines()
#     print(s)

# # OSError: [Errno 22] Invalid argument: 'file_for_hw8\numbers.txt'

with open('file_for_hw8/numbers.txt', encoding='utf-8') as file1:
    res = 0
    for line in file1:
        string = [int(sym) for sym in line if sym.isdigit()]
        res += sum(string)

with open('file_for_hw8/answer.txt', 'a', encoding='utf-8') as file2:
    print(res)

# FileNotFoundError: [Errno 2] No such file or directory: 'file_for_hw8/numbers.txt'