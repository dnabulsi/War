import random
from time import sleep

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
          'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    '''
    Define the card's suit (Hearts, Diamonds, Spades, Clubs)
    and rank, value is determined automatically via global dictionary
    '''

    def __init__(self,suit,rank):
        self.suit = suit.capitalize()
        self.rank = rank.capitalize()
        self.value = values[rank.capitalize()]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    '''
    Create the deck of cards, with suits and ranks
    '''

    def __init__(self):
       
        # Initialize an empty deck of cards as a list
        self.all_cards = []

        # Loop through all suits
        for suit in suits:
            # Loop through all ranks
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))

    def shuffle(self):
        # Shuffle the deck of cards
        random.shuffle(self.all_cards)

    def deal_one(self):
        # Deal one card from the deck
        return self.all_cards.pop()

class Player():
    '''
    Create a player class consisting of the name, cards owned,
    and functions to remove and add cards, and print total amount of cards
    '''

    def __init__(self,name):
        self.name = name.title()
        self.all_cards = []
    
    def remove_one(self):
        # Pop the first element from the list of all cards
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        # If new_cards contains more than one object as a list
        if type(new_cards) == type([]):
            return self.all_cards.extend(new_cards)
        # If new_cards is one object
        return self.all_cards.append(new_cards)

    def __str__(self):
        # If the player has one card
        if len(self.all_cards) == 1:
            # Return this statement
            return f'Player {self.name} has {len(self.all_cards)} card.'
        # Otherwise return this statement
        return f'Player {self.name} has {len(self.all_cards)} cards.'
        
# Initialize my_deck and shuffle it
my_deck = Deck()
my_deck.shuffle()

# Ask user for input on first player's name
player1_name = input("What is the name of the first player? ")
# Initialize first player
player1 = Player(player1_name)
# Ask user for input on second player's name
player2_name = input("What is the name of the second player? ")
# Initialize second player
player2 = Player(player2_name)

# Divide deck amongst both players
while my_deck.all_cards:
    # If player1 has more cards than player2
    if len(player1.all_cards) > len(player2.all_cards):
        # Deal the next card to player2
        player2.add_cards(my_deck.deal_one())
    else:
        # Otherwise deal the card to player1
        player1.add_cards(my_deck.deal_one())

round = 0

# Infinite loop to represent rounds
while True:
    
    round += 1
    print(f"Round {round}:")

    # Check if either player has 0 cards, break if so
    if not player1.all_cards:
        print(f"{player1.name} is out of cards. {player2.name} wins!")
        quit()

    elif not player2.all_cards:
        print(f"{player2.name} is out of cards. {player1.name} wins!")
        quit()

    # Initialize player1_cards and player2_cards from each player's deck
    player1_cards = []
    player1_cards.append(player1.remove_one())
    player2_cards = []
    player2_cards.append(player2.remove_one())

    while True:
        if player1_cards[-1].value > player2_cards[-1].value:
            print(f"{player1.name}'s card, {player1_cards[-1]}, is greater than {player2.name}'s card, {player2_cards[-1]}. {player1.name} wins the round!")
            player1.add_cards(player1_cards)
            player1.add_cards(player2_cards)
            break
        elif player1_cards[-1].value < player2_cards[-1].value:
            print(f"{player2.name}'s card, {player2_cards[-1]}, is greater than {player1.name}'s card, {player1_cards[-1]}. {player2.name} wins the round!")
            player2.add_cards(player2_cards)
            player2.add_cards(player1_cards)
            break
        else:
            print(f"WAR: {player2.name}'s card, {player2_cards[-1]}, is equal to {player1.name}'s card, {player1_cards[-1]}. Each player must draw 5 cards.")
            sleep(0.5)
            for x in range(5):
                try:
                    player1_cards.append(player1.remove_one())
                except:
                    print(f"{player1.name} does not have enough cards for war. {player2.name} wins!")
                    quit()
                try:
                    player2_cards.append(player2.remove_one())
                except:
                    print(f"{player2.name} does not have enough cards for war. {player2.name} wins!")
                    quit()
            print(f"Both players have successfully drawn 5 cards from their deck.")
            sleep(0.5)
    
    print(player1)
    print(f"{player2}\n")
    sleep(0.5)