profit = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
financial_result = profit - costs
profitability = financial_result /profit
print(profitability)
employees_number = int(input('Введите колличество сотрудников: '))
profit_per_emmloyee = costs / employees_number
print('Прибыль фирмы в расчете на одного сотрудника = ' + f'{profit_per_emmloyee}')