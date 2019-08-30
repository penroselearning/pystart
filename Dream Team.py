players = ['Stephen Curry', 'LeBron James', 'Michael Jordan', 'Kobe Bryant', 'James Harden']
x = 1

print("Basketball Dream Team:")
print('-' * 30)
for player in players:
    print(f'{x}.{player}')
    x += 1

while True:
    x = 1
    print()
    action = int(input('''Would you like to:
1. Add a Player
2. Remove a Player
3. View Team
4. Exit
---------------------
Please choose the number corresponding to the action of your choice.\n'''))
    print()

    if action == 1:
        item = input("Enter a New Basketball Player\n").title()
        players.append(item)
        print()
        print("Updated Team:")
        print('-' * 30)
        for player in players:
            print(f'{x}.{player}')
            x += 1

    elif action == 2:
        item = input("Enter a Player you Wish to Remove from your Team\n").title()
        players.remove(item)
        print()
        print("Updated Team:")
        print('-' * 30)
        for player in players:
            print(f'{x}.{player}')
            x += 1

    elif action == 3:
        print("Basketball Dream Team:")
        print('-' * 30)
        for player in players:
            print(f'{x}.{player}')
            x += 1
    elif action == 4:
        exit()

    else:
        print("Sorry that is an invalid response. Please choose a number between 1 and 4.")
