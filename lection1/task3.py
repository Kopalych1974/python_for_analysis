# Приложение для определения знака зодиака по дате рождения.

'''
Задание 3.
Разработать приложение для определения знака зодиака по дате рождения.
Пример:

Введите месяц: март
Введите число: 6

Вывод:
Рыбы

Дата рождения                   Знак Зодиака

с 21 марта по 20 апреля         Овен

с 21 апреля по 20 мая           Телец

с 21 мая по 21 июня             Близнецы

с 22 июня по 22 июля            Рак

с 23 июля по 23 августа         Лев

с 24 августа по 23 сентября     Дева

с 24 сентября по 23 октября     Весы

с 24 октября по 22 ноября       Скорпион

с 23 ноября по 21 декабря       Стрелец

с 22 декабря по 20 января       Козерог

с 21 января по 20 февраля       Водолей

с 21 февраля по 20 марта        Рыбы

'''

month_of_bith = str(input("Введите месяц: "))
day_of_bith = int(input("Введите дату рождения: "))


if (month_of_bith == "Март" and 21 <= day_of_bith <= 31) or (month_of_bith == "Апрель" and 1 <= day_of_bith <= 20):
    print("По знаку зодиака Вы - Овен")

elif (month_of_bith == "Апрель" and 21 <= day_of_bith <= 30) or (month_of_bith == "Май" and 1 <= day_of_bith <= 20):
    print("По знаку зодиака Вы - Телец")

elif (month_of_bith == "Май" and 21 <= day_of_bith <= 31) or (month_of_bith == "Июнь" and 1 <= day_of_bith <= 21):
    print("По знаку зодиака Вы - Близнецы")

elif (month_of_bith == "Июнь" and 22 <= day_of_bith <= 30) or (month_of_bith == "Июль" and 1 <= day_of_bith <= 2):
    print("По знаку зодиака Вы - Рак")

elif (month_of_bith == "Июль" and 23 <= day_of_bith <= 31) or (month_of_bith == "Август" and 1 <= day_of_bith <= 23):
    print("По знаку зодиака Вы - Лев")

elif (month_of_bith == "Август" and 24 <= day_of_bith <= 31) or (month_of_bith == "Сентябрь" and 1 <= day_of_bith <= 23):
    print("По знаку зодиака Вы - Дева")

elif (month_of_bith == "Сентябрь" and 24 <= day_of_bith <= 30) or  (month_of_bith == "Октябрь" and 1 <= day_of_bith <= 23):
    print("По знаку зодиака Вы - Весы")

elif (month_of_bith == "Октябрь" and 24 <= day_of_bith <= 31) or (month_of_bith == "Ноябрь" and 1 <= day_of_bith <= 22):
    print("По знаку зодиака Вы - Скорпион")

elif (month_of_bith == "Ноябрь" and 23 <= day_of_bith <= 30) or (month_of_bith == "Декабрь" and 1 <= day_of_bith <= 21):
    print("По знаку зодиака Вы - Стрелец")

elif (month_of_bith == "Декабрь" and 22 <= day_of_bith <= 31) or (month_of_bith == "Январь" and 1 <= day_of_bith <= 20):
    print("По знаку зодиака Вы - Козерог")

elif (month_of_bith == "Январь" and 21 <= day_of_bith <= 31) or (month_of_bith == "Февраль" and 1 <= day_of_bith <= 20):
    print("По знаку зодиака Вы - Водолей")

else:
    print("По знаку зодиака Вы - Рыбы")
