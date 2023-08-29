# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.

import random
print('\n Программа определяет минимальное количество монеток, \n которые нужно перевернуть так, чтобы все лежали одной стороной.')
print('(Соотношение выпавших "орла" и "решки" определяется по случайному закону)\n')

count_m = int(input("Введите количество монет: "))
print('Ваш вариант:')
orel = 0
resh = 0
for i in range(count_m):
    orel_resh = random.randint(0, 1)
    if orel_resh == 1: 
        orel += 1
    else: 
        resh += 1
    print(orel_resh, end=' ')
if orel <= resh:
    print(f'\nНадо перевернуть {orel} монет(ы)\n')
else:
    print(f'\nНадо перевернуть {resh} монет(ы)\n')


