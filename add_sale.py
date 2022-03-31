from sys import argv


sale = argv[1]
with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.write(f'{sale}\n')
