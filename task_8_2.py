import re


f_name = 'nginx_logs.txt'
with open(f_name, 'r', encoding='utf-8') as f:
    for row in f:
        line = row
        pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+)\s-\s-\s.(\d+/\w+/\w+:\w+:\w+:\w+\s[+]\w+).\s"(\w+)\s(.\w+.\w+)\s\w+.\w+.\w+.\s(\d+\s\d+)')
        all_result = pattern.findall(line)
        print(all_result)