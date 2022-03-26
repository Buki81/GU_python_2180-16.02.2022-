def odd_number(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


number = odd_number(5)

print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))