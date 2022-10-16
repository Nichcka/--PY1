money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
delta = 0 #разница между зарплатой и тратами за месяц

while money_capital >= spend:
    delta = salary - spend
    money_capital += delta #остаток подушки после трат
    month += 1
    spend *= (1+increase)

print(month)
