word = input("Enter a Word of your Choice:\n")
reverse=''
word_count=len(word)

for letter in range(word_count):
    reverse += word[word_count-1]
    word_count -= 1

print(f'{word} when reversed reads {reverse}')
