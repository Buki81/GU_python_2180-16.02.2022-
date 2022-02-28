# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
# случайных слов, взятых из трёх списков (по одному из каждого)
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# добавить еще один аргумент — флаг, разрешающий или запрещающий повторы

from random import choices as ch


def get_jokes(num, replay=True):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    ns, av, ad = nouns, adverbs, adjectives
    words = ' '.join(ch(ns)+ ch(av)+ ch(ad))
    joke = [' '.join(ch(ns)+ ch(av)+ ch(ad)) for i in range(num)]

    if replay:
        print(joke)
    else:
        number = 0
        while number != num * 3:
            words = ' '.join(ch(ns)+ ch(av)+ ch(ad))
            joke = [' '.join(ch(ns)+ ch(av)+ ch(ad)) for i in range(num)]
            number = len(set(' '.join(joke).split()))
        print(joke)


get_jokes(4, replay=False)



