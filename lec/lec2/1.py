list_1 = []
list_1 = list ()
print  (list_1)
list_1 = [1,2,3,8]
print  (list_1)   
print  (*list_1)   # *бкз скобочек
for i in list_1:  #списком
    print(i)
print(len(list_1)) #длина списка
print(list_1[3]) #обращение к конкретному элементу 
print(list_1[-1]) #обращение к конкретному элементу 

list_1.append(10) #добавить к списку что-то
print  (*list_1)

# пример
list_2 =[]
print  (*list_2)
for i in range (5):
    list_2.append(i)
    print  (*list_2)
    
    