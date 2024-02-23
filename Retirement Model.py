import numpy_financial as npf

salary = 60000
savings_rate = 0.25
investment_rate = 0.05
desired_cash = 1500000

annual_cash = salary * savings_rate

print(annual_cash)

years_to_retirement = npf.nper(investment_rate, -annual_cash, 0, desired_cash)
#print("Number of years to retirement:", years_to_retirement)
#for(i=0; i< years_to_retirement.)
print("Martha has" , years_to_retirement, " years to retirement")
#print(f'Martha has {years_to_retirement:.If} years to retirement.')