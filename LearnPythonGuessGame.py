secret_word = "respect"
guess = ''
guess_count = 0
guess_limit = 7
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("What's the secret word?: ")
        guess_count += 1
        if guess != secret_word:
            print("Hint: " + secret_word[int(guess_count)-1])

    else:
        out_of_guesses = True

if out_of_guesses:
    print("All out of guesses, better luck next time!")
    exit()
else:
    print("Nice work!")
    exit()