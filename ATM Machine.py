PASSWORD='12345@'
account_balance=60000

attempts=3
pin=input("Enter your Account Pin:\n")
attempts -= 1

while pin!=PASSWORD:
  if attempts > 0:
      pin = input(f'''Sorry, the password is incorrect.You have {attempts} more attempt/s.
Please enter your Account Pin again:\n''')
      attempts -= 1
  else:
      print('Sorry, you have entered an incorrect password 3 times. Your account has been blocked :-(')
      exit()

print('-'*30)
print("Welcome to your Account.")

action= int(input('''Would you like to:
1. Deposit Money
2. Withdraw Money
3. View Balance
------------------------
Please choose the number corresponding to the action of your choice:\n'''))

if action == 1:
  amount = int(input('How much money would you like to deposit in your account (USD). Please type the number:\n'))
  account_balance += amount
  print(f'Your new account balance is USD {account_balance}')
elif action == 2:
  amount = int(input('How much money would you like to withdraw from your account (USD). Please type the number:\n'))
  account_balance -= amount
  print(f'Your new account balance is USD {account_balance}')
elif action == 3:
  print(f'Your current account balance is USD {account_balance}')

print('Thank you!')