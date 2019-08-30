# Add, Remove and Insert Items into your List

shopping_list = ['Eggs', 'Brown Bread', 'Apple Juice', 'Strawberries', 'Cookies']

while True:

    print()
    action = int(input('''Would you like to:
1. Add an Item
2. Remove an Item
3. View the Cart
4. Exit
---------------------
Please choose the number corresponding to the action of your choice.\n'''))
    print()

    if action == 1:
        item = input("Enter a New Shopping List Item\n").title()
        shopping_list.append(item)

        print('-' * 30)
        print("Updated Shopping List after Adding New Item")
        print('-' * 30)
        for shopping_item in shopping_list:
            print(shopping_item)

    elif action == 2:
        item = input("Enter Item you wish to Remove from your List\n").title()

        if item not in shopping_list:
            print(f"Sorry, {item} does not exist in your Cart")
        else:
            shopping_list.remove(item)

            print('-' * 30)
            print("Updated Shopping List after Removing an Item")
            print('-' * 30)
            for shopping_item in shopping_list:
                print(shopping_item)

    elif action == 3:
        print('-' * 30)
        print("Shopping List")
        print('-' * 30)
        for shopping_item in shopping_list:
            print(shopping_item)
        print('-' * 30)

    else:
        exit()