def time_to_seconds(years, weeks, days, hours, mins):
    totalmins = (years * 525600) + (weeks * 10080) + (days * 1440) + (hours * 60) + mins
    totalseconds = totalmins * 60
    return totalseconds


print("Time Convertor")
print('-' * 30)

years = int(input('Enter Years:\n'))
weeks = int(input('Enter Weeks (1-53):\n'))
days = int(input('Enter Days: (1-6)\n'))
hours = int(input('Enter Hours: (1-23)\n'))
mins = int(input('Enter Minutes: (1-59)\n'))

totalseconds = time_to_seconds(years, weeks, days, hours, mins)

print()
print(f'''{years} year(s), {weeks} week(s), {days} day(s), {hours} hour(s)
and {mins} minute(s) equals {totalseconds:,} second(s).''')

