import random

compscore=0
playerscore=0

for x in range(5):
  computer = random.randint(1,5)

  print(f'Round {x+1}')
  guess= int(input('Please guess a number from 1 to 5:\n'))

  if guess==computer:
    print('Congratulations! You guessed correctly.')
    playerscore+=1
  else:
    print(f'Sorry you did not guess correctly. The computer chose {computer}')
    compscore+=1

  print('\n')
  print(f'''The score after this round is: 
----------------------------------------
Computer - {compscore}
You - {playerscore}''')
  print('\n')


if compscore>playerscore:
  print(f'Sorry, you have Lost the Game. Better Luck next time')
elif compscore==playerscore:
  print(f'Its a draw.')
elif compscore<playerscore:
  print(f'Congratulations, You have Won!!!')

print(f'''
The final score is: 
------------------------------------
Computer - {compscore}
You - {playerscore}
''')