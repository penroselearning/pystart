from datetime import datetime,timedelta
import calendar

today = datetime.now()

print()

try:
    birth_year = int(input("Enter Birth Year:"))
    birth_month = int(input("Enter Birth Month (1-12):"))
    birth_day = int(input("Enter Birth Day:"))
    bday = (f'{birth_day}-{birth_month}-{birth_year}')
    birthday = datetime.strptime(bday, '%d-%m-%Y')

except:
    print("Incorrect Date")
    exit()
else:
    print(f"You were born on a {datetime.strftime(birthday, '%A')}")
    print()

    currentyear = datetime.strftime(today, '%Y')
    thisyearbday = (f'{birth_day}-{birth_month}-{currentyear}')
    thisyear_birthday = datetime.strptime(thisyearbday, '%d-%m-%Y')

    if thisyear_birthday > today:
        nextbday = (thisyear_birthday - today) + timedelta(days=1)
    elif thisyear_birthday < today:
        nextbday = ((datetime.strptime(thisyearbday, '%d-%m-%Y') + timedelta(days=365)) - today) + timedelta(days=1)
    else:
        print('Something went wrong.')

    weekdays = []
    tdays = 0
    for x in range(5):
        if calendar.isleap(int(currentyear) + (x + 1)):
            tdays += 366
        else:
            tdays += 365

        bdays = thisyear_birthday + timedelta(days=tdays)
        weekdays.append(datetime.strftime(bdays, '%A-%d-%B-%Y'))

    print(f'No. of days till next birthday: {nextbday.days} days {nextbday.seconds//3600} hours and {nextbday.seconds%3600} minutes')
    print()
    print(f'Day of week for next 5 birthdays:{weekdays}')
