# Домашнее задание к лекции 1.1 «Основы Python»

# Задание 4.
# Нужно разработать приложение для финансового планирования.
# Приложение учитывает сколько уходит на ипотеку, “на жизнь” и сколько нужно отложить на пенсию.
# Пользователь вводит заработанную плату в месяц.
# Сколько процентов от зп уходит на ипотеку.
# Сколько процентов от зп уходит “на жизнь”.
# Сколько раз приходит премия в год.
# Остальная часть заработанной платы откладывается на пенсию.
# Также пользователю приходит премия в размере зарплаты, от которой половина уходит на отпуск, а вторая половина откладывается.
# Программа должна учитывать сколько премий было в год.
# Нужно вывести сколько денег тратит пользователь на ипотеку и сколько он накопит за год.
# Пример:
# 
# Введите заработанную плату в месяц: 100000
# Введите сколько процентов уходит на ипотеку: 30
# Введите сколько процентов уходит на жизнь: 50
# Введите количество премий за год: 2
# 
# Вывод:
# На ипотеку было потрачено: 360000 рублей
# Было накоплено: 340000 рублей

monthly_net = int(input("Please enter your monthly net income: "))
interest_mortgage = int(input("Enter how much interest is spent on a mortgage: "))
recurrent_payments = int(input("Enter a percentage of recurrent payments: "))
number_of_bonuses = int(input("Enter the number of bonuses per year: "))

# Считаем зарплату за год
total_yearly_net = monthly_net * 12

total_mortgage = (total_yearly_net * interest_mortgage)/100

total_recurrent_payments = (total_yearly_net * recurrent_payments)/100
total_of_bonuses = monthly_net *number_of_bonuses

accumulated_amount = total_yearly_net -  total_recurrent_payments - total_mortgage
accumulated_amount_total = total_of_bonuses/2 + accumulated_amount
print("Total:")
print("Total mortgage: ", total_mortgage, "RUR")
print("Accumulated Amount: ", accumulated_amount_total, "RUR")
