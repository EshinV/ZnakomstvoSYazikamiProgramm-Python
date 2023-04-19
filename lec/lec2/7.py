# Операции со множествами в Python:
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8} - 
print(c)
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21) только уникальные значения, поэтому только 1 раз будет 2
print(u)
i = a.intersection(b) # i = {8, 2, 5} переcечения
print(i)
dl = a.difference(b) # dl = {1, 3} разность
print(dl)
dr = b.difference(a) # dr = {13, 21} 
print(dr)
q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13}   сначала пересечение a b, потом разность и затем обьединяем 
print(q)

# Множества
# Неизменяемое или замороженное множество(frozenset) — множество, с которым не будут
# работать методы удаления и добавления.
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})
