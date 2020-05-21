# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

if month == 1:
    print('31 days in January')
elif month == 2:
    print('28 days in February')
elif month == 3:
    print('31 days in March')
elif month == 4:
    print('30 days in April')
elif month == 5:
    print('31 days in May')
elif month == 6:
    print('30 days in June')
elif month == 7:
    print('31 days in July')
elif month == 8:
    print('31 days in August')
elif month == 9:
    print('30 days in September')
elif month == 10:
    print('31 days in October')
elif month == 11:
    print('30 days in November')
elif month == 12:
    print('31 days in December')
else:
    print(month, 'incorrect input')
