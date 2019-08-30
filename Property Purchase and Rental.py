from datetime import datetime,timedelta

date_of_purchase = '02-Jan-2019'
date_of_purchase = datetime.strptime(date_of_purchase,'%d-%b-%Y')

def interest_calculator():
  loaninterest= (property_price*loan_period*interest_rate)/100
  totalpayment= property_price+loaninterest
  return totalpayment

property_price = 500000
loan_period = 15
interest_rate = 8
year=1

totalamount= interest_calculator()
rent=0

while totalamount >= rent:
  rent += 24000*1.05**year
  year += 1


investment_recovery_date = (date_of_purchase + timedelta(days=year*365)).strftime('%b %Y')

print(f'The approximate date that David will recover his money is {investment_recovery_date}.')

