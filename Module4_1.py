from fake_math import divide as divnull #импорт функции и назначили другое название
from true_math import divide as divinf  #импорт функции из другого модуля и назначили другое название


# вызовы функций по их новым названиям

print(divnull(69, 3))
print(divnull(3, 0))

print(divinf(49, 7))
print(divinf(15, 0))


