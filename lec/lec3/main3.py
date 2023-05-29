import modul3
print(modul3.max1(5,9))

# или

from modul3 import max1
print(max1(10,3))

# чтоб импортировать сразу все функции ставь *

from modul3 import *
print(max1(22,13))

# с переименованием модуля

import modul3 as m1
print(m1.max1(44,9))