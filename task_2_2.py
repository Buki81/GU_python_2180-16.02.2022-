# Дан список. Необходимо его обработать —
# обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов

import copy

list_temp = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была',
             '+5', 'градусов']

for i in range(len(list_temp)):
    if any(k in '1234567890'for k in list_temp[i]):
        if int(list_temp[i]) < 10:
            num_list = list(list_temp[i])
            num_list.insert(-1, '0')
            list_temp[i] = ''.join(num_list)

for i in copy.deepcopy(list_temp):
    if any(k in '1234567890'for k in i):
        a = list_temp.index(i)
        list_temp.insert(a, '"')
        list_temp.insert(a+2, '"')

print(list_temp)

# Сформировать из обработанного списка строку:
for i in list_temp:
    if i == '"':
        list_temp.remove(i)

for i in range(len(list_temp)):
    if any(k in '1234567890'for k in list_temp[i]):
        num_list = list(list_temp[i])
        num_list.insert(0, '"')
        num_list.insert(len(list_temp), '"')
        list_temp[i] = ''.join(num_list)

print(' '.join(list_temp))
