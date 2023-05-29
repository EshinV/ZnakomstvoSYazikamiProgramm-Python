def quick_sort(array):
    if len(array) <=1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <=pivot]
    greater = [i for i in array[1:] if i >pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([10,5,2]))

# Описание работы программы
# Быстрая сортировка
# ● 1-е повторение рекурсии:
# ○ array = [10, 5, 2, 3]
# ○ pivot = 10
# ○ less = [5, 2, 3]
# ○ greater = []
# ○ return quicksort([5, 2, 3]) + [10] + quicksort([])
# ● 2-е повторение рекурсии:
# ○ array = [5, 2, 3]
# ○ pivot = 5
# ○ less = [2, 3]
# ○ greater = []
# ○ return quicksort([2, 3]) + [5] + quicksort([]) # Важно! Не забывайте, что здесь помимо вызова рекурсии
# добавляется список [10]
# ● 3-е повторение рекурсии:
# ○ array = [2, 3]
# ○ return [2, 3] # Сработал базовый случай рекурсии
# На этом работа рекурсии завершилась и итоговый список будет выглядеть таким образом: [2, 3] + [5] + [10] = [2, 3, 5,
# 10]