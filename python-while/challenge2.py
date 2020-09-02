#challenge2.py

import random

guessnumber = 0
count = 0
value = random.randint(1, 10)

print("Guess a number between 1 and 10")

while guessnumber != value:
    count += 1
    guessnumber = input(f'Enter guess #{count}: ')
    if guessnumber.isnumeric() == False:
        print('Numbers only, please!')


    elif int(guessnumber) < int(value):
        print('Your guess is too low, try again!')

    elif int(guessnumber) > int(value):
        print('Your guess is too high, try again!')

    elif int(guessnumber) == int(value):
        print(f'You guessed it in {count} tries!')
        exit()


