# Реализовать вывод информации о промежутке времени
# в зависимости от его продолжительности
# duration в секундах: до минуты: <s> сек;
# до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = 400153

day = duration // (3600 * 24)
hour = (duration - day * 3600 * 24) // 3600
min = (duration - hour * 3600 - day * 3600 * 24) // 60
sec = duration % 60

if duration < 60:
    print(sec, 'сек')
elif duration < 3600:
    print(min, 'мин', sec, 'сек')
elif duration < 3600 * 24:
    print(hour, 'час', min, 'мин', sec, 'сек')
else:
    print(day, 'дн',hour, 'час', min, 'мин', sec, 'сек')
