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

# Now the required classes for the logic.

# Hand class


class Hand(object):

    def __init__(self, cards=None, value=0):
        self.value = value
        self.cards = cards if cards is not None else []

    def count(self):
        '''
        Counts the value of the player's hand and adds to the value
        '''
        flag = False  # If the flag value is True, then there is an 'A' card in the hand.
        for card in self.cards:
            if card[0] == 'A':
                flag = True
                continue  # skips A, to check it later.
            self.value += values[card[0]]
        if flag:
            if self.value + 11 > 21:
                values['A'] = 1
                self.value += 1
            else:
                self.value += 11

    def get_cards(self):
        return self.cards

    def get_value(self):
        return self.value

    def set_value(self, newval):
        self.value = newval

    def add_card(self, card):
        self.cards.append(card)

# Player class


class Player(object):

    def __init__(self, hand=None):
        self.hand = hand if hand is not None else Hand()

    def hit(self):
        '''
        Adds a card to the player's hand
        '''
        shuffle(deck)
        self.hand.add_card(deck[0])

    def get_hand(self):
        return self.hand

# Clear screen function


def clear_screen():
    '''
    Clear screen
    '''
    if sys.platform == "linux" or sys.platform == "linux2":
        os.system('clear')
    elif sys.platform == "win32":
        os.system('cls')

# Main game function


def game():
    # Creating the two Player objects

    player = Player()
    dealer = Player()
    # Dealing the first 2 cards the player and 1 card to the dealer

    player.hit()
    player.hit()
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

    def play_again():
        print("\nDo you wish to play again? (Y)es (N)o")
        option = input()
        if option.lower() == 'y':
            game()
        elif option.lower() == 'n':
            clear_screen()
            return
        else:
            clear_screen()
            print("Invalid, please say 'y' or 'n'")
            play_again()

    player.get_hand().count()
    if player.get_hand().get_value() == 21:
        clear_screen()
        print_info()
        print("Congratulations! You got blackjack!")
        play_again()
        return

    # main loop
    while True:

        while True:
            clear_screen()
            print_info()
            print("Do you wish to (s)tand or to (h)it?")
            option = input()
            if option.lower() in ['s', 'stand']:
                # If the player stood while he was losing, it means the player gave up.
                if dealer.get_hand().get_value() > player.get_hand().get_value():
                    clear_screen()
                    print_info()
                    print("You gave up!")
                    break
                # If the player is standing, all there's left to do is deal cards to the dealer and stop when the value of the dealer's hand is greater than (or equal to, if the player's hand value is 21, resulting in a draw) the player's hand value.
                while dealer.get_hand().get_value() <= player.get_hand().get_value():
                    dealer.hit()
                    dealer.get_hand().count()
                    clear_screen()
                    print_info()
                    if dealer.get_hand().get_value() > 21:
                        print("The dealer bursts! You win!")
                        break
                    elif dealer.get_hand().get_value() > player.get_hand().get_value():
                        print("You lost!")
                        break
                    elif dealer.get_hand().get_value() == player.get_hand().get_value() == 21:
                        print("It's a draw!")
                        break
                    # The AI doesn't want a draw unless there's no choice! So it won't stop hitting unless it's a 21-to-21 draw.
                break
            elif option.lower() in ['h', 'hit']:
                player.hit()
                player.get_hand().count()
                clear_screen()
                print_info()
                if player.get_hand().get_value() > 21:
                    print("You burst! You lose!")
                    break

        play_again()
        return


game()
