def odd_number(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


number = 15
print(*odd_number(number)) # 1 3 5 7 9 11 13 15

gen_num = (num for num in range(1, number+1, 2))
print(*gen_num) # 1 3 5 7 9 11 13 15
