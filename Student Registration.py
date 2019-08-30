from datetime import datetime

registrations = {}
registration_date = datetime.now()

while True:
    action = int(input('''Would you like to:
1. Register for the event or,
2. Exit
Please choose a number:\n'''))
    print()

    if action == 1:
        student_name = input("Enter Student Name:\n").title()
        print()
        print(f'{"Name":20} {"Registration Date"}')
        print('-' * 47)
        registrations.update({student_name: registration_date})

        for name, regdate in registrations.items():
            print(f'{name:20} {regdate}')
        print()

    elif action == 2:
        exit()
    else:
        print('Sorry that is an invalid response.')
        print()

