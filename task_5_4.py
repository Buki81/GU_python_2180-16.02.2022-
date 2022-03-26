import sys
from time import perf_counter


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123]

start = perf_counter()
result = [el_2 for el_1, el_2 in zip(src[:-1], src[1:]) if el_1 < el_2]
print(result, perf_counter() - start, sys.getsizeof(result))
# [12, 44, 4, 10, 78, 123] 1.7700018361210823e-05 120

'''Другое решение'''
def two(src_2):
    a,*rest = src_2
    return [el_2 for el_1, el_2 in zip(src_2, rest) if el_1 < el_2]

print(two(src), perf_counter() - start, sys.getsizeof(result))
# [12, 44, 4, 10, 78, 123] 0.00020730006508529186 120
