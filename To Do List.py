packing_list=[]

while True:

    item_count = 0
    for line in open('packinglist.txt'):
        item_count +=1

    action = int(input('''Would you like to:
    1. Add an item
    2. View all items
    3. Search for an item
    4. Exit
    Please choose a number from 1-4.\n'''))
    print()

    if action == 1:
        newitem = input('What would you like to add to the list:\n').title()
        with open('packinglist.txt', 'a') as file:
            file.write(f'{item_count+1}.{newitem}\n')
        print()
        with open("packinglist.txt", 'r') as file:
            print(file.read())

    elif action == 2:
        with open("packinglist.txt", 'r') as file:
            print(file.read())

    elif action == 3:
        search_item = input("Search Packing List for: ").title()

        if search_item in open('packinglist.txt').read():
            print(f"Yes, {search_item} is in the list.")
        else:
            print(f"No, {search_item} is not in the list")
    elif action == 4:
        exit()
    else:
        print("Sorry, Incorrect Choice")
