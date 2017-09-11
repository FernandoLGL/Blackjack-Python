from random import shuffle
import os
import sys

'''
This Blackjack project is supposed to be basic, including only 'Hit' and 'Stand'.
'''
values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'K': 10, 'Q': 10}
suits = ['S', 'D', 'C', 'H']

keys_values = list(values.keys())  # variable that defines all the values a card can have (list)
deck = [card_value + suit for card_value in keys_values for suit in suits]  # all the cards possible (list)
# shuffle(deck)  I don't need to shuffle the deck now because everytime a player hits, it's shuffled.

# Now the required classes for the logic.


class Hand(object):

    def __init__(self, cards=None, value=0):
        self.value = value
        self.cards = cards if cards is not None else []

    def count(self):
        '''
        Counts the value of the player's hand and adds to the value
        '''
        for card in self.cards:
            if card[0] == 'A' and self.value + 11 > 21:
                values['A'] = 1
            else:
                values['A'] = 11

            self.value += values[card[0]]

    def get_cards(self):
        return self.cards

    def get_value(self):
        return self.value

    def set_value(self, newval):
        self.value = newval

    def add_card(self, card):
        self.cards.append(card)


class Player(object):

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

# main function


def game():

    # Creating the two players objects
    player = Player()
    dealer = Player()

    # Dealing the first 2 cards to each player
    player.hit()
    player.hit()
    dealer.hit()
    dealer.hit()

    def print_cards(p):
        '''
        Function to print the cards in a hand properly.
        INPUT: Player
        OUTPUT: String
        '''
        out = ''
        for elem in p.get_hand().get_cards():
            out += elem + ' '
        return out

    def print_info():
        '''
        Function to print all the information of the players.
        '''
        player.get_hand().set_value(0)
        dealer.get_hand().set_value(0)
        player.get_hand().count()
        dealer.get_hand().count()
        print("Player's cards: {c} Value: {v}\n".format(c=print_cards(player), v=player.get_hand().get_value()))
        print("Dealer's cards: {c} Value: {v}\n".format(c=print_cards(dealer), v=dealer.get_hand().get_value()))
    # main loop
    while True:

        clear_screen()
        print_info()

        while True:
            print("Do you wish to 'stand' or to 'hit'?")
            option = input()
            if option.lower() == 'stand':

                # If the player is standing, all there's left to do is deal cards to the dealer and stop when the value of the dealer's hand is greater than (or equal to, if the player's hand value is 21, resulting in a draw) the player's hand value.
                while True:
                    dealer.hit()
                    dealer.get_hand().count()
                    clear_screen()
                    print_info()
                    if dealer.get_hand().get_value() > 21:
                        print("The dealer bursts! You win!")
                        return
                    elif dealer.get_hand().get_value() > player.get_hand().get_value():
                        print("You lost!")
                        return
                    elif dealer.get_hand().get_value() < player.get_hand().get_value():
                        print("You win!")
                        return
                    elif dealer.get_hand().get_value() == player.get_hand().get_value() == 21:
                        print("It's a draw!")
                        return
                    # The AI doesn't want a draw unless there's no choice! So it won't stop hitting unless it's a 21-to-21 draw.

            elif option.lower() == 'hit':
                player.hit()
                player.get_hand().count()
                clear_screen()
                print_info()
                if player.get_hand().get_value() > 21:
                    print("You burst! You lose!")
                    return
            else:
                clear_screen()
                print("Please enter 'stand' or 'hit'!")


game()
