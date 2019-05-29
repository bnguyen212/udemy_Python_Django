#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        self.pile = [(num, suite) for num in RANKS for suite in SUITE];
        shuffle(self.pile);

    def split(self):
        return (self.pile[:26], self.pile[26:])

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = cards

    def add_cards(self, cards):
        self.cards.extend(cards)

    def remove_card(self):
        if len(self.cards) > 0:
            return self.cards.pop(0);

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play(self):
        return self.hand.remove_card()

    def has_cards(self):
        return len(self.hand.cards) > 0

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
deck = Deck()
halves = deck.split()
player = Player(input("Please enter your name: "), Hand(halves[0]))
computer = Player("Computer", Hand(halves[1]))
temp_deck = [];

while player.has_cards() and computer.has_cards():
    print("*"*20)
    print("Player currently has {} cards in hand".format(len(player.hand.cards)))
    print("Computer currently has {} cards in hand".format(len(computer.hand.cards)))

    player_card = player.play()
    print("Brian played: ", player_card)
    comp_card = computer.play()
    print("Computer played: ", comp_card)
    temp_deck.append(player_card)
    temp_deck.append(comp_card)

    if player_card[0] == comp_card[0]:
        temp_deck.extend([player.play(), player.play(
        ), player.play(), computer.play(), computer.play(), computer.play()])
        print("It's a tie, each loses 3 cards!")
    else:
        if RANKS.index(player_card[0]) > RANKS.index(comp_card[0]):
            player.hand.add_cards(temp_deck)
            print("Player won this round")
        else:
            computer.hand.add_cards(temp_deck)
            print("Computer won this round")
        temp_deck.clear()

    decision = input("Continue? (y/n)")
    if decision == 'n':
        break


print("Game Ended")



# Use the 3 classes along with some logic to play a game of war!
