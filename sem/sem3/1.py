# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
a = [1, 1, 2, 0, -1, 3, 4, 4]
b = set (a)
print(len(b))


# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

c = [1, 2, 3, 4, 5]
k = int(input ('Vvedite shag: '))

for i in range(k):       
    c.append(c.pop(0))
print(c)

print(c[k:]+c[:k])