import json


def glossary():
    with open(f1_name, encoding='utf-8') as f1:
        with open(f2_name, encoding='utf-8') as f2:
            interests = {}
            for users, hobby in zip(f1.read().splitlines(), f2.read().splitlines()):
                interests[users] = hobby
            with open(f3_name, 'w', encoding='utf-8') as f:
                f.write(json.dumps(interests))


f1_name = 'users.csv'
f2_name = 'hobby.csv'
f3_name = 'hobby_dic.csv'

lines1, lines2 = 0, 0
for line in open(f1_name, encoding='utf-8'):
    lines1 += 1
for line in open(f2_name, encoding='utf-8'):
    lines2 += 1

if lines1 == lines2:
    glossary()
elif lines1 > lines2:
    for i in range(1, lines1 - lines2 + 1):
        with open(f2_name, 'a', encoding='utf-8') as f:
            f.writelines('\nNone')
        glossary()
else:
    print(1/0)


with open(f3_name, encoding='utf-8') as f:
    print(json.loads(f.read()))

