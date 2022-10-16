salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for i in range(months):
    need = spend - salary  # нужно денег, чтобы прожить в i-ом месяце
    spend = spend + spend * increase  # траты в следующем мсесяце
    need_money += need

print(round(need_money))
