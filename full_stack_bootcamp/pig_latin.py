# pig_latin.py


original = input("What word would you like me to translate?\n")

word = original.lower()

first = word[0]

if first in 'aeiou':
    new_word = word + 'yay'
    print(new_word)
else:
    new_word = word[1:] + first + 'ay'
    print(new_word)
