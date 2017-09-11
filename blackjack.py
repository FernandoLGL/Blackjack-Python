from random import shuffle
import os
import sys

# TODO: Logic behind blackjack and defining which methods and classes will be needed

values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'K': 10, 'Q': 10}
suits = ['S', 'D', 'C', 'H']

keys_values = list(values.keys())  # variable that defines all the values a card can have (list)
deck = [card_value + suit for card_value in keys_values for suit in suits]  # all the cards possible (list)
# shuffle(deck)  I don't need to shuffle the deck now because everytime a player hits, it's shuffled.

# Now the required classes for the logic.


class Hand(object):
    # Class Hand is all tested.
    def __init__(self, cards=None, value=0):
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
    # Class Player is all tested.
    # Class Object Attribute that informs if  the player is standing or not
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
    # We should only call this function if both players p1 and p2 are standing.
    p1_value = p1.get_hand().count()
    p2_value = p2.get_hand().count()
    if p1_value > p2_value or p1_value < p2_value:
        return True
    else:
        return False

# main function


def game():


game()
