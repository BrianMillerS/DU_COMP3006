#!/usr/bin/env python3

suits = ['♠', '♥', '♦', '♣']
values = [14,13,12,11,10,9,8,7,6,5,4,3,2] # 14 = Ace, 13 = king, etc...

deck_of_cards = list(zip(suits*13, values*4))


print("This deck has {} cards".format(len(deck_of_cards)))
print(deck_of_cards)
