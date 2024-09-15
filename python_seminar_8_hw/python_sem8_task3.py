# Задача 3. Турнир
# В файле first_tour.txt записано число K и данные об участниках турнира по
# настольной игре «Орлеан»: фамилии, имена и количество баллов, набранных в
# первом туре. Во второй тур проходят участники, которые набрали более K
# баллов в первом туре.
# Напишите программу, которая выводит в файл second_tour.txt данные всех
# участников, прошедших во второй тур, с нумерацией.
# В первой строке нужно вывести в файл second_tour.txt количество участников
# второго тура. Затем программа должна вывести фамилии, инициалы и
# количество баллов всех участников, прошедших во второй тур, с нумерацией.
# Имя нужно сократить до одной буквы. Список должен быть отсортирован по
# убыванию набранных баллов.
# Пример:
# Содержимое файла first_tour.txt:
# 80
# Ivanov Serg 80
# Sergeev Petr 92
# Petrov Vasiliy 98
# Vasiliev Maxim 78
# Содержимое файла second_tour.txt:
# 2
# 1) V. Petrov 98
# 2) P. Sergeev 92



with open("python_seminar_8_hw/file_for_hw8/first_tour.txt", "r", encoding="utf-8") as ft:
    txt = list(ft.readlines()) # ['80\n', 'Ivanov Serg 80\n', 'Sergeev Petr 92\n', 'Petrov Vasiliy 98\n', 'Vasiliev Maxim 78']
    k = int(txt[0]) # 80
    dict_player = dict()
    for i in range(1, len(txt)):
        data = txt[i].split()
        key = str(int(data[2]))
        dict_player[key] = f'{data[1][0]}. {data[0]}'

# print(dict_player) -> {'80': 'S. Ivanov', '92': 'P. Sergeev', '98': 'V. Petrov', '78': 'M. Vasiliev'}

count = 0
second_tour = {}
for key, value in dict_player.items():
    if int(key) > 80:
        second_tour[key] = dict_player[key]
        count += 1
sorted_sec_tour = sorted(second_tour.items(), reverse=True)



with open("python_seminar_8_hw/file_for_hw8/second_tour.txt", "w", encoding="utf-8") as st:
    print(count, file = st)
    for i, value in enumerate(sorted_sec_tour, start = 1):
        print(i, ') ', *value, file = st)
