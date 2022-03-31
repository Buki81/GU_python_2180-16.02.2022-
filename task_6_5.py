# реализовать интерфейс командной строки, чтобы можно было
# задать имя обоих исходных файлов и имя выходного файла

def glossary(f1, f2, f3):
    with open(f1, encoding='utf-8') as f1:
        with open(f2, encoding='utf-8') as f2:
            for users, hobby in zip(f1.read().splitlines(), f2.read().splitlines()):
                with open(f3, 'a', encoding='utf-8') as f:
                    f.write(f'{users}: {hobby}\n')

def f_name(f1, f2, f3):
    lines1, lines2 = 0, 0
    for line in open(f1, encoding='utf-8'):
        lines1 += 1
    for line in open(f2, encoding='utf-8'):
        lines2 += 1

    if lines1 == lines2:
        glossary(f1, f2, f3)
    elif lines1 > lines2:
        for i in range(1, lines1 - lines2 + 1):
            with open(f2, 'a', encoding='utf-8') as f:
                f.writelines('\nNone')
            glossary(f1, f2, f3)
    else:
        print(1/0)


    with open(f3, encoding='utf-8') as f:
        print(f.read())

if __name__ == '__main__':
    f_name('users.csv', 'hobby.csv', 'users_hobby.txt')
