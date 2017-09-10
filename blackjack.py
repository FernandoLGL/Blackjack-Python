from random import shuffle
import os
import sys

# TODO: Logic behind blackjack and defining which methods and classes will be needed

values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'K': 10, 'Q': 10}
suits = ['S', 'D', 'C', 'H']

keys_values = list(values.keys())  # variable that defines all the values a card can have
deck = [card_value + suit for card_value in keys_values for suit in suits]  # all the cards possible
shuffle(deck)  # shuffling so the deck is now ready.

# Now the required classes for the logic.


class Hand(object):
    def __init__(self, value=0, cards=None):
        self.value = value
        self.cards = cards if cards is not None else []

    def count(self):
        '''
        Counts the value of the player's hand
        '''
        for card in self.cards:
            if card[0] == 'A' and self.value + 11 > 21:
                values['A'] = 1
            else:
                values['A'] = 11

            self.value += values[card[0]]

        return self.value

    def get_cards(self):
        return self.cards

    def get_value(self):
        return self.value

    def add_card(self, card):
        self.cards.append(card)


class Player(object):

    stand = False

    def __init__(self, hand=None):
        self.hand = hand if hand is not None else Hand()

    def hit(self, pos=0):
        '''
        Adds a card to the player's hand
        '''
        shuffle(deck)
        self.hand.add_card(deck[pos])

    def get_hand(self):
        return self.hand


def clear_screen():
    '''
    Clear screen
    '''
    if sys.platform == "linux" or sys.platform == "linux2":
        os.system('clear')
    elif sys.platform == "win32":
        os.system('cls')


def check_win(p1, p2):
    '''
    Compare 2 player's hands and check if there's a winner.
    '''
    p1_value = p1.get_hand().count()
    p2_value = p2.get_hand().count()
    if p1_value > p2_value or p1_value < p2_value:
        return True
    else:
        return False

# main function


def game():
    # 2 player objects
    dealer = Player()
    player = Player()
    # give 2 cards to each player
    dealer.hit()
    dealer.hit()
    player.hit()
    player.hit()


game()
