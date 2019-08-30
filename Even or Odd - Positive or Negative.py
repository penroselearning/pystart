n1 = int(input("Enter a Number of your Choice: "))

if n1 > 0:
    result1 = 'positive'
elif n1 < 0:
    result1 = 'negative'
else:
    result1 = 'zero'
if n1 % 2 == 0:
    result2 = 'even'
else:
    result2 = 'odd'

print(f"{n1} is {result1} and an {result2} number.")