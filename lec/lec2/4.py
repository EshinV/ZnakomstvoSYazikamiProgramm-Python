# Кортежи
# Кортеж — это неизменяемый список.

t = () # создание пустого кортежа
print(type(t)) # class <'tuple'>
t = (1,)
print(type(t))
t = (1)
print(type(t))
t = (28, 9, 1990)
print(type(t))

v=[1,8,9]
print(v)
print(type(v))

v=tuple(v)
print(v)
print(type(v))

# a, b = 1, 2
# a=b=1

a,b,c = v
print(a,b,c)

t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue))# r:red g:green b:blue
print(t[2])
#если написать t[0] = 2 то он выдаст ошибку и не даст перименовать, так как значение нельзя изза формата tuple
for i in t:
    print(i)

for i in range(len(t)):
    print(t[i])


