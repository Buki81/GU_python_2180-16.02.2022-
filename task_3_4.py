thesaurus_adv =("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {"А": {"П": ["Петр Алексеев"]}, "И": {"И": ["Илья Иванов"]}, "С": {"И": ["Иван Сергеев",
# "Инна Серова"], "А": ["Анна Савельева"]}}


def thesaurus(name):
    surname = {}
    letter_sur = {i.split(' ')[1][0] for i in name} # Выбор первых букв фамилии
    for el in letter_sur:
        list_surname = []
        for i in name:
            if el in i[1:]:
                list_surname.append(i)
        surname[el] = list_surname

        letter = {i[0] for i in list_surname} # Выбор первых букв имени
        forename = {}
        for j in letter:
            list_name = []
            for k in list_surname:
                if j in k[:1]:
                    list_name.append(k)
            forename[j] = list_name
        surname[el] = forename

    print(surname)

thesaurus(thesaurus_adv)
# {'И': {'И': ['Илья Иванов']},
# 'С': {'А': ['Анна Савельева'],
# 'И': ['Иван Сергеев', 'Инна Серова']},
# 'А': {'П': ['Петр Алексеев']}}
