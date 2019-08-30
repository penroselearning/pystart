cars = [('Honda', 'Accord', 'Blue', 2019),
        ('Nissan', 'Patrol', 'Black', 2018),
        ('Infiniti', 'QX60', 'Silver', 2018)]

action = int(input('''Would you like to:
1. Add a Car
2. Remove a Car
3. View Cars
4. Exit
---------------------
Please choose the number corresponding to the action of your choice.\n'''))
print()

if action == 1:
    make = input("Enter a New Car Make:\n").title()
    model = input("Enter The Car Model:\n").title()
    color = input("Enter The Car Color:\n").title()
    year = input("Enter The Car Year:\n").title()

    print()
    cars.append((make, model, color, year))

    print(f'{"Make":20} {"Model":20} {"Color":20} {"Year":20}')
    print('-' * 70)
    for info in cars:
        print(f'{info[0]:20} {info[1]:20} {info[2]:20} {info[3]}')

elif action == 2:
    make = input("Enter the make of the car you wish to remove:\n").title()
    print()
    for x in range(len(cars)):
        if make == cars[x][0]:
            cars.pop(x)
            break
    else:
        print("Not Found")

    print(f'{"Make":20} {"Model":20} {"Color":20} {"Year":20}')
    print('-' * 70)
    for info in cars:
        print(f'{info[0]:20} {info[1]:20} {info[2]:20} {info[3]}')

elif action == 3:
    print(f'{"Make":20} {"Model":20} {"Color":20} {"Year":20}')
    print('-' * 70)
    for info in cars:
        print(f'{info[0]:20} {info[1]:20} {info[2]:20} {info[3]}')

elif action == 4:
    exit()

else:
    print("Sorry that is an invalid response. Please choose a number between 1 and 4.")