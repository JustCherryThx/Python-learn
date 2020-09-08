import random

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

deck = []

for suit in suits:
  for rank in ranks:
    deck.append(f'{rank} of {suit}')

deck1 = len(deck)

print(f'There are {deck1} cards in the deck.')

print('Dealing...')

print(f'There are {deck1 - 5} cards in the deck.')

card_selects = random.choices(deck, k=5)
print('Player has the following cards in their hand: ')
print(card_selects)
exit()


