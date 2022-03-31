from sys import argv

with open('bakery.csv', encoding ='UTF-8') as f:
    if len(argv) == 1:
        print(f.read())
    elif len(argv) == 2:
        for i, line in enumerate(f):
            if (i + 1) >= int(argv[1]):
                print(line, end='')
    elif len(argv) == 3:
        for i, line in enumerate(f):
            if int(argv[1]) <= (i + 1) <= int(argv[2]):
                print(line, end='')
            # print(i + 1)
