import random

football_teams=['Brazil','Argentina',
                'England','Belgium','Germany','Italy','Spain',
                'France','Sweden','Switzerland','Croatia','Portugal']

team1 = random.choice(football_teams)

team2 = random.choice(football_teams)

if team1 == team2:
    team2 = random.choice(football_teams)

football_friendly = f'{team1} vs {team2}'

print(football_friendly)