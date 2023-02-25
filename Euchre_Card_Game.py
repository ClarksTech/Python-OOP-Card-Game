from random import shuffle

# class to represent a card
class card:
    suit = ["Hearts", "Spades", "Diamonds", "Clubs"]

    value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    # create the card structure when the class is initalised
    def __init__(self, s, v):
        self.suit = s
        self.value = v

# class to represent the deck of cards
class deck:

    # create the deck of cards when the deck object is initialised
    def __init__(self):
        self.cards = []
        for s in range(4):
            for v in range(13):
                self.cards.append(card(s,v))

        # shuffle the deck of cards so not in order
        shuffle(self.cards)

        # return a random card from the deck and remove from deck
        def rdmCard(self):
            if len(self.cards) == 0:
                return
            return self.cards.pop()

# class to keep track of player cards and wins
class player: 
    def __init__(self, name):
        self.wins = 0
        self.cards = None
        self.name = name

# class to contain euchre game logic
class game: 


