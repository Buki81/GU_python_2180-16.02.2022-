f_name = 'nginx_logs.txt'

with open(f_name, 'r', encoding='utf-8') as f:
    a = {}
    for rows in f.readlines():
        num = str(rows.split('"-"')[0].split('1.1"')[1:])[7:-3]
        if num.isnumeric():
            a[int(num)] = rows.split(' - - ')[0]
    print(a[max(list(a))], max(list(a)))
# 5.9.121.211 86377168
