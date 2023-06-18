amount = 0
tickets = int(input("Количество билетов:\n"))
for age in range(tickets):
    age = int(input("Возраст:\n"))
    if age < 18:
        amount += 0
    elif age >= 18 and age <= 25:
        amount += 990
    elif age > 25:
        amount += 1390
if amount == 0:
    print("Вход свободный")
else:
    print("Количествово билетов:", tickets, "шт." )
if tickets > 3 :
    discount = amount / 100 * 10
    print("Скидка:", "%.2f" % discount, "руб.")
    print("К оплате:", "%.2f" % (amount -discount), "руб.")
