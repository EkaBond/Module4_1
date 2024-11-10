def divide(first, second):  #ф-я принимает два значения
   if second == 0:          # вернет слово "ошибка" если во вторую переменную зададим ноль
       return 'Ошибка'
   else:
       return first / second   # иначе вернет результат деления
