money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while True:
    money_capital += salary - spend  # подушка безопасности в конце месяца
    spend *= 1 + increase  # траты в следующем месяце

    if money_capital <= 0:
        break

    month += 1

print(month)
