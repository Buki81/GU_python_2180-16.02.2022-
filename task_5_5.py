import sys
from time import perf_counter


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]



'''Решение <в лоб>'''
start = perf_counter()
simply = [i for i in src if src.count(i)==1]
print(simply, perf_counter() - start, sys.getsizeof(simply))
# [23, 1, 3, 10, 4, 11] 2.2599997464567423e-05 120

'''Другое решение'''
start = perf_counter()
result = [src[i] for i in range(len(src)) if (src[i] in list(src[i+1:]) or src[i] in list(src[:i])) == False]
print(result, perf_counter() - start, sys.getsizeof(result))
# [23, 1, 3, 10, 4, 11] 0.0002457000082358718 120

'''Третий вариант'''
start = perf_counter()
briefly = list(filter(lambda x: src.count(x) == 1, src))
print(briefly, perf_counter() - start, sys.getsizeof(briefly))
# [23, 1, 3, 10, 4, 11] 0.0003645999822765589 120

'''С множеством'''
start = perf_counter()
unique_num = set()
for num in src:
    if num in unique_num:
        unique_num.discard(num)
        continue
    unique_num.add(num)
print([num for num in src if num in unique_num], perf_counter() - start, sys.getsizeof(unique_num))
# [23, 1, 3, 10, 4, 11] 1.960000372491777e-05 728



