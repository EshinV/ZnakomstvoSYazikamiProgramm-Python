# Множества содержат в себе уникальные элементы, не обязательно упорядоченные.
# Одно множество может содержать значения любых типов. Если у Вас есть два множества,
# Вы можете совершать над ними любые стандартные операции, например, объединение,
# пересечение и разность. Давайте разберем их.
colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('red')  # -ничего не добавится
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok
colors.clear()
print(colors)

q=set() #-строка  (преобразовать в множество из строки например)
