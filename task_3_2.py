# Доработать предыдущую функцию в num_translate_adv(): реализовать
# корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
# Например:
# >>> num_translate_adv("One") "Один"
# >>> num_translate_adv("two") "два"
# word[0].isupper() istitle
# word[0].capitalize()
dic_translate = {'null' : 'ноль', 'zero' : 'ноль', 'one' : 'один',
                 'two' : 'два', 'three' : 'три', 'four' : 'четыре',
                 'five' : 'пять', 'six' : 'шесть', 'seven' : 'семь',
                 'eight' : 'восемь', 'nine' : 'девять', 'ten' : 'десять'}


def num_translate_adv(word):
    if word.istitle() and dic_translate.get(word.lower()):
        print(dic_translate.get(word.lower()).capitalize())
    else:
        print(dic_translate.get(word))


num_translate_adv('Five') # Пять
num_translate_adv('Five1') # None
num_translate_adv('five') # пять
num_translate_adv('five1') # None
