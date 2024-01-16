def money(deposit, monthly_income, tax, years):

    
    money = deposit
    
    for year in range(years):
        money += 12 * monthly_income
        money += money / 100 * tax
    return money

print(money(15000, 500, 45, 5))