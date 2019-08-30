cookie_menu = {'Chocolate Chip': 2,
               'Peanut Butter': 2.5,
               'Ginger Bread': 2,
               'Shortbread': 1.5}

while True:
    print('Cookie Menu')
    print('-' * 20)
    for food, price in cookie_menu.items():
        print(f'{food:15} USD {price}')

    bill = 0
    print()
    order = input("Kindly place your Order:\n").title()

    if order in cookie_menu.keys():

        quantity = int(input(f'How Many {order} cookies do you wish to Order?\n'))

        for cookie_menu, price in cookie_menu.items():
            if cookie_menu == order:
                bill += price

        total = (bill * quantity) * 1.05

        print()
        print('-' * 30)
        print(f'The Total Bill Amount is $ {round(total, 2)}')
        break

    else:
        print(f'Sorry, Wrong Order!! We do not sell {order}')

    print()



