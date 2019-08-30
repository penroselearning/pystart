vacations = {'Vienna' : [2010,'Austria','Schönbrunn Palace', 'Apple Strudel']}

while True:
    print()
    action = int(input('''Would you like to:
1. Add a Vacation Detail
2. View the Vacation List
3. Exit
---------------------
Please choose the number corresponding to the action of your choice.\n'''))

    if action == 1:
        vacations.update({input('City Name:\n'):
                          [int(input('Year of Visit:\n')),
                           input('Country:\n'),
                           input('Favorite Spot:\n'),
                           input('Favorite Food:\n')]})

    elif action == 2:

        print(f'{"City":15} {"Year of Visit":13} {"Country":15} {"Favorite Spot":25} {"Favorite Food":25}')
        for city,info in vacations.items():
            print(f'{city:15} {info[0]:13} {info[1]:15} {info[2]:25} {info[3]:25}')

    elif action == 3:
        exit()

    else:
        print("Sorry that is an invalid response. Please choose a number between 1 and 3.")



