import random

olympic_boxers = ['Mary Kom','Nicola Adams','Claressa Sheilds',
'Marlen Esparza','Natasha Jonas','Ren Cancan',
'Savannah Marshall','Mary Spencer']

olympic_boxers_copy = olympic_boxers.copy()

matches=[]

if len(olympic_boxers) % 2 != 0:
    print("Sorry, you need to have an Even Number of Boxers to schedule the Matchups")
else:
    for x in range(len(olympic_boxers)//2):
        boxer1 = random.choice(olympic_boxers_copy)
        olympic_boxers_copy.remove(boxer1)

        boxer2 = random.choice(olympic_boxers_copy)
        olympic_boxers_copy.remove(boxer2)

        matches.append(f'{boxer1} vs {boxer2}')

    print("Boxing Matches - Round 1")
    print('-'*30)
    for match in matches:
        print(match)