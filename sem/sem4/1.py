# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()


# x = input("Введите чтонибудь: ")
# print(x)
# print(type(x))
# y=x.split() #преобразует в список (по умолчанию в скобках стоит разделитель пробел " ")   можно поставить любой разделитель, НР , 
# print(y)
# print(type(y))

# my_str = ""
# for i in range(5):
#     my_str+='_'+str(i)
# print(my_str)

string = input("Введите строку: ")
chars = {}
for char in string.split():
    if char in chars: #проверка сивола в слловаре 
        chars[char] += 1
        char += "_" + str(chars[char])
    else:
        chars[char] = 0

    print(char, end=" ") # end=" " - разделитель 

# способ 2
# my_str = "a a a b c a a d c d d".split()
# result_str = ''
# for i in range(len(my_str)):
#     print (i)
#     print(my_str[:i])
#     print(my_str[:i].count(my_str[i]))

my_list = 'a a a b c a a d c d d'.split()
result_str = ''
for i in range(len(my_list)):
    print(my_list[:i])
    print(my_list[:i].count(my_list[i]))
    print('-' * 15)
    if len(result_str) == 0:
        result_str = my_list[i]
    elif my_list[:i].count(my_list[i]) == 0:
        result_str += ' ' + my_list[i]
    else:
        result_str += ' _' + my_list[i] + str(my_list[:i].count(my_list[i]))

print(result_str)
