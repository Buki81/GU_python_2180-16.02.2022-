f_name = 'nginx_logs.txt'

with open(f_name, 'r', encoding='utf-8') as f:
    logs = []
    for row in f:
        row_1 = row[:95].split(' - - ')[0]
        row_2 = row[:95].split(' - - ')[1].split(' "')[1].split('" ')[0].split(' ')
        row_tp = (row_1, row_2[0], row_2[1])
        logs.append(row_tp)
    print(logs)
