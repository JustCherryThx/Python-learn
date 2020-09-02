#challenge1.py

import random

guessnumber = 0
count = 0
value = random.randint(1, 5)


while guessnumber != value:
    count += 1
    guessnumber= input("Guess a number between 1 and 5: ")
    if guessnumber.isnumeric():
        guessnumber = int(guessnumber)


else:
    print(f'You guessed it in {count} tries!')
    exit()