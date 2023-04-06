username = input ("Введите имя: ")
if username == 'Маша':
    print("Ура, это же МАША! ")
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username =='Ильнар' :

    print('Ильнар -Ton) ')
else:
    print('Привет, ', username)
    

n = 423
summa = 0
while n > 0:
    x = n % 10
    summa = summa + x
    n = n // 10
    if n <=0:
        break
else:
    print('Пожалуй')
    print('хватит )')
print(summa)

n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0: # если остаток при делении числа n на i равен 0
        flag = False
        print(i)
    elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
        print(n)
        flag = False
    i += 1