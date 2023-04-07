a=5
b= 5.89
c = 'hello'

print(a,'-',b,'-',c)
print(f"{a} - {b} {c}")
print ("{} - {} -{}".format(a,b,c))


#input    #-ввод данных
print ('Vvedite chislo')
e = int(input ()   )
print (e)

f = int(input ('Vvefite 2e chislo: '))
print (f)


print(e, '+', f,'=',e+f)

g = 5.89
print(g)
print(type(g))
g = int(g) #перевели в нужный формат (из строки (букв) нельзя привести к типу int)
print(g)
print(type(g))

