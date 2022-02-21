# Создать список, состоящий из кубов нечётных чисел от 1 до 1000
# Вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму,
# так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
#
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17
# и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список

import copy
list_cube = [i**3 for i in range(1, 1000) if i%2 != 0]
print(list_cube)
sum_cube = 0

for i in list_cube:
    number = 0
    i_dc = copy.deepcopy(i)
    while i_dc > 0:
        number += i_dc % 10
        i_dc = i_dc // 10
    if number % 7 == 0:
        sum_cube += i

print(sum_cube)
print('---------------------------')

#* Решить задачу под пунктом b, не создавая новый список
sum_cube_17 = 0

for i in list_cube:
    i = i + 17
    number = 0
    i_dc = copy.deepcopy(i)
    while i_dc > 0:
        number += i_dc % 10
        i_dc = i_dc // 10
    if number % 7 == 0:
        sum_cube_17 += i

print(sum_cube_17)
