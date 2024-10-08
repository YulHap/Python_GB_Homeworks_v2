# Урок 3. Списки и словари
# Task 1. Встречаемость элемента в массиве
# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.
# Пример:
# list_1 = [1, 2, 3, 4, 5]
# k = 3
# Вывод: 1

# Решение 1: 

list_1 = [1, 2, 3, 4, 5]
k = 3

count = 0
for i in range(len(list_1)): 
    if list_1[i] == k:
        count += 1
print(count)

# Решение 2: 

list_1 = [1, 2, 3, 4, 5]
k = 3
print(list_1.count(k))

# Заимствованные решения:

# Решение 1: 

list_1 = [1, 2, 3, 4, 5]
k = 3

total = 0

for i in list_1:
    if i == k:
        total += 1

print(total)
