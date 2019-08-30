def aspect_ratio_calculator(width, height):
    action = int(input('''Would you like to enter a:
    1. New width
    2. New Height
    Please choose 1 or 2.'''))

    print()

    if action == 1:
        newwidth = int(input("New Width:\n"))
        if newwidth > width:
            finalheight = int((newwidth / width) * height)
        elif newwidth < width:
            finalheight = int(height / (width / newwidth))
        print()
        print(f'''New Dimensions:
-------------------
Width: {newwidth}
Height: {finalheight}''')

    elif action == 2:
        newheight = int(input("New Height:\n"))
        if newheight > height:
            finalwidth = int((newheight / height) * width)
        elif newheight < height:
            finalwidth = int(width / (height / newheight))
        print()
        print(f'''New Dimensions:
-------------------
Width: {finalwidth}
Height: {newheight}''')

    else:
        print('Sorry invalid response.')


width = int(input("Current Width:\n"))
height = int(input("Current Height:\n"))

aspect_ratio_calculator(width, height)

print()