# Задача №1. Общее обсуждение
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2
print ('Задача №1')
n = 700
m = 700
print ((m+n-1)//n)


# Задача №3. Общее обсуждение
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

print ('Задача №3')
a = int(input ('Vvedite kol ychrnikov iz 1 klassa: '))
b = int(input ('Vvedite kol ychrnikov iz 2 klassa: '))
c = int(input ('Vvedite kol ychrnikov iz 3 klassa: '))

# full = a+b+c
# if full%2==1:
#     print((full//2)+1)
# else:
#     print(full//2)
    

print(a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)



# Задача №5. Решение в группах
# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

print ('Задача №5')

i = int(input ('Vvedite номер вагона вити '))
j = int(input ('Vvedite номер на табличке: '))
if j==i:
    print ("невозможно узнать")
else:
    print (j-1+i)
    
# 1 2 3 4 5 6 7
#         3


# Задача №7. Решение в группах
# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES
print ('Задача №7')

f = int(input ('Vvedite god '))

if f%4==0 and (f%400==0 or f%100!=0):
    print ("da")
else:
    print ("no")