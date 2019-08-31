import csv
import os.path

def save_file(fieldnames, filename):
    file_exists = os.path.isfile(filename)

    with open(filename, 'a') as csvfile:
        csvEntry = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if file_exists is False:
            csvEntry.writeheader()

        csvEntry.writerow({
            'name': input("Enter a New Disease Name:\n").title(),
            'year': int(input("Enter the Year of Last Occurence:\n")),
            'country': input("Enter the Country of Last Occurence:\n").title(),
            'vaccine': input("Enter the Founder of the Vaccine:\n").title()
        })
        print()


def view_file(fieldnames, filename):
    with open("eradicated_diseases.csv") as csvfile:
        csvReader = csv.DictReader(csvfile, delimiter=',', fieldnames=fieldnames)

        eradicated_diseases = list(csvReader)
        print(
            f'{"Disease Name":15} {"Last Occurence (Year)":25} {"Last Occurence (Country)":25} {"Vaccine Founder"}')

        for disease in eradicated_diseases:
            if disease['name'] != 'name':
                print(f'{disease["name"]:15} {disease["year"]:25} {disease["country"]:25} {disease["vaccine"]}')


def search_file(fieldnames, filename):
    with open("eradicated_diseases.csv") as csvfile:
        csvReader = csv.DictReader(csvfile, delimiter=',', fieldnames=fieldnames)
        print()
        eradicated_diseases = list(csvReader)
        search_item = input("Search Disease List for:\n").title()

        found = False
        for disease in eradicated_diseases:
            if search_item in disease["name"]:
                found = True

        if found is True:
            print(f"Yes,{search_item} is in the list")
        else:
            print(f"No,{search_item} is not in the list")


print("Eradicated Diseases List")
print("-" * 30)

fieldnames = ['name', 'year', 'country', 'vaccine']
filename = 'eradicated_diseases.csv'

selection = 0
while True:
    selection = int(input('''
Enter Option Number
--------------------
1. Add Disease
2. View Disease List
3. Search for a Disease
4. Exit Program\n'''))
    print()

    if selection == 1:
        save_file(fieldnames, filename)
    elif selection == 2:
        view_file(fieldnames, filename)
    elif selection == 3:
        search_file(fieldnames, filename)
    elif selection == 4:
        exit()
    else:
        print("Wrong Selection")
