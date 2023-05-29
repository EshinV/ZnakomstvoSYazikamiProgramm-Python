# def - функция

def sum_numbers(n, y = 'Hello'):
    print(y)
    summa = 0
    for i in range(1, n+1):
        summa +=i
    return summa
    print ("stop")  #после return программа прерывается

a = sum_numbers (5, 'qwert')
print (a)


# функция с неограниченным кол-вом аргументов

def sum_str(*args):
    res = ''
    for i in args:
        res+=i
    return res
print(sum_str('q','e','l'))
print(sum_str('q','e','l','r','f'))