# Задача №13. Решение в группах
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

import random 

print('Задача №13  ')
n_days = int(input('Введите число: '))
count = 0
m=0
prev = None
temps = []
for i in range(n_days): #-цикл перебора
    temp = random.randint(-50,50)
    # print (temp, end = " ")  
    temps.append(temp)
    
    # if temp>0:
    #     count=count+1
    #     prev = temp
    # else: m =count
    

print (temps)
maxLong = 0
currLong = 0
for temp in temps:
     if temp > 0:
        currLong = currLong +1
     else:
        if currLong > maxLong:
            maxLong = currLong
        currLong = 0
print ("\n", maxLong)


# import random   - с лекции сокращённый

# n_days = int(input("Введите кол-во дней: "))
# temps = [] 
# for i in range(n_days): 
#     temp = random.randint(-50, 50)
#     temps.append(temp)
# print(temps)
# maxLong = 0
# currLong = 0
# for temp in temps:
#     if temp > 0:
#         currLong = currLong +1
#     else:
#         if currLong > maxLong:
#             maxLong = currLong
#         currLong = 0
# print(maxLong)