# Урок 3. Списки и словари
# Task 3. Скрабл
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# Пример:
# k = 'ноутбук'
# Вывод: 12

# Решение: 

k = 'ноутбук'

letter = {}
letter["A"] = 1
letter["B"] = 3
letter["C"] = 3
letter["D"] = 2
letter["E"] = 1
letter["F"] = 4
letter["G"] = 8
letter["H"] = 4
letter["I"] = 1
letter["J"] = 2
letter["K"] = 5
letter["L"] = 1
letter["M"] = 3
letter["N"] = 1
letter["O"] = 1
letter["P"] = 3
letter["Q"] = 10
letter["R"] = 1
letter["S"] = 1
letter["T"] = 1
letter["U"] = 1
letter["V"] = 4
letter["W"] = 4
letter["X"] = 8
letter["Y"] = 4
letter["Z"] = 10

letter["А"] = 1
letter["Б"] = 3
letter["В"] = 1
letter["Г"] = 3
letter["Д"] = 2
letter["Е"] = 1
letter["Ё"] = 3
letter["Ж"] = 5
letter["З"] = 5
letter["И"] = 1
letter["Й"] = 4
letter["К"] = 2
letter["Л"] = 2
letter["М"] = 2
letter["Н"] = 1
letter["О"] = 1
letter["П"] = 2
letter["Р"] = 1
letter["С"] = 1
letter["Т"] = 1
letter["У"] = 2
letter["Ф"] = 10
letter["Х"] = 5
letter["Ц"] = 5
letter["Ч"] = 5
letter["Ш"] = 8
letter["Щ"] = 10
letter["Ь"] = 3
letter["Ы"] = 4
letter["Ъ"] = 10
letter["Э"] = 8
letter["Ю"] = 8
letter["Я"] = 3

k = k.upper()
i = 0
count = 0

while i < len(k):
    count += letter[k[i]]
    i += 1
print(count)
