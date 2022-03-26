def students(pupils, classroom):
    for i in range(1, len(pupils) - len(classroom) + 1):
        classroom.append('None')
    return ((el_1, el_2) for el_1, el_2 in zip(pupils, classroom))


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий']
klasses = ['9А', '7В', '9Б']

print(*students(tutors, klasses), sep='\n')
print(students(tutors, klasses))
# ('Иван', '9А')
# ('Анастасия', '7В')
# ('Петр', '9Б')
# ('Сергей', 'None')
# ('Дмитрий', 'None')
# <generator object students.<locals>.<genexpr> at 0x00000147103F1F50>
