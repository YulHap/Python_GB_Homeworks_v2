# Урок 3. Списки и словари
# Task 2. Ближайший элемент в массиве
# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.
# Пример:
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# Вывод: 5

# Решение: 

list_1 = [1, 2, 3, 4, 5]
k = 6

razn1 = 0
l0 = list_1[0]
min1 = k - l0
bliz1 = list_1[0]

razn2 = 0
min2 = l0 - k
bliz2 = list_1[0]

bliz = list_1[0]

if min1 < 0:
    min1 *= -1
if min2 < 0:
    min2 *= -1

for i in range(1, len(list_1)):
    li = list_1[i]
    razn1 = k - li
    razn2 = li - k
    if razn1 < 0:
        razn1 *= -1
    if razn2 < 0:
        razn2 *= -1
    if razn1 < min1:
        min1 = razn1
        bliz1 = li
    if razn2 < min2:
        min2 = razn2
        bliz2 = li

if min1 < min2:
    print(bliz1)
else:
    print(bliz2)