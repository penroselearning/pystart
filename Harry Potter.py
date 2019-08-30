harry_potter_movies={'The Sorcerers Stone': 7.6,
'The Chamber of Secrets': 7.4,
'The Prisoner of Azkaban': 7.9,
'The Goblet of Fire': 7.7,
'The Order of the Pheonix': 7.5,
'The Half-Blood Prince': 7.6,
'The Deathly Hallows Part 1': 7.7,
'The Deathly Hallows Part 2': 8.1}

print("Harry Potter Movies & Ratings")
print('-'*40)

for movies,rating in harry_potter_movies.items():
  print(f'{movies.title():35} {rating}')