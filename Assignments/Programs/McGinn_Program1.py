"""
David McGinn
2-15-17
2143 OOP

This program allows the user to "play" a game of "War"
against the computer
"""

import os
import random
import time

CARD = """\
_________
|{}     |
|       |
|   {}  |
|       |
|     {}|
_________
""".format('{trank:^2}', '{suit: <2}', '{brank:^2}')

TEN = """\
_________
|{}    |
|       |
|   {}  |
|       |
|    {}|
_________
""".format('{trank:^3}', '{suit: <2}', '{brank:^3}')

FACECARD = """\
_________
|{}|
|       |
|   {}  |
|       |
|{}|
_________
""".format('{trank:<7}', '{suit: <2}', '{brank:>7}')

HIDDEN_CARD = """\
_________
|???????|
|???????|
|???????|
|???????|
|???????|
_________
"""

class Card(object):
    
    def __init__(self, suit, rank):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param rank: The value of the card, e.g 3 or King
        """

        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King","Ace"]



        self.card_values = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'Jack': 11,
            'Queen': 12,
            'King': 13,
            'Ace': 14  
        }

        self.str_values = {
            '2': CARD,
            '3': CARD,
            '4': CARD,
            '5': CARD,
            '6': CARD,
            '7': CARD,
            '8': CARD,
            '9': CARD,
            '10': TEN,
            'Jack': FACECARD,
            'Queen': FACECARD,
            'King': FACECARD,
            'Ace': FACECARD,  # value of the ace is high until it needs to be low
        }

        self.suits = ['Spades','Hearts','Diamonds','Clubs']

        self.symbols = {
            'Spades':   'S',
            'Diamonds': 'D',
            'Hearts':   'H',
            'Clubs':    'C',
        }


        if type(suit) is int:
            self.suit = self.suits[suit]
        else:
            self.suit = suit.capitalize()
        self.rank = str(rank)
        self.symbol = self.symbols[self.suit]
        self.points = self.card_values[str(rank)]
        self.ascii = self.__str__()
    

    def __str__(self):
        symbol = self.symbols[self.suit]
        trank = self.rank+symbol
        brank = symbol+self.rank
        return self.str_values[self.rank].format(trank=trank, suit=symbol,brank=brank)
           
    def __cmp__(self,other):
        return self.points < other.points 
   
    # Python3 wasn't liking the __cmp__ to sort the cards, so 
    # documentation told me to use the __lt__ (less than) 
    # method.
    def __lt__(self,other):
        return self.__cmp__(other)

"""
@Class Deck 
@Description:
    This class represents a deck of cards. 
@Methods:
    pop_cards() - removes a card from top of deck
    add_card(card) - adds a card to bottom of deck
    shuffle() - shuffles deck
    sort() - sorts the deck based on value, not suit (could probaly be improved based on need)
"""       
class Deck(object):
    def __init__(self):
        #assume top of deck = 0th element
        self.cards = []
        for suit in range(4):
            for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King","Ace"]:
                self.cards.append(Card(suit,rank))
                
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "".join(res)
    
    def pop_card(self):
        return self.cards.pop(0)
        
    def add_card(self,card):
        self.cards.append(card)
        
    def shuffle(self):
        random.shuffle(self.cards)
    
    def sort(self):
        self.cards = sorted(self.cards)

class Hand(list):
    def __init__(self, cards=None):
        """Initialize the class"""
        super().__init__()
        if (cards is not None):
            self._list = list(cards)
        else:
            self._list = []
    
    def __str__(self):
        return self.join_lines()

    def join_lines(self):
        """
        Stack strings horizontally.
        This doesn't keep lines aligned unless the preceding lines have the same length.
        :param strings: Strings to stack
        :return: String consisting of the horizontally stacked input
        """
        liness = [card.ascii.splitlines() for card in self._list]
        return '\n'.join(''.join(lines) for lines in zip(*liness))
        
    def add(self,card):
        self._list.append(card)
        
    def sort(self):
        self._list = sorted(self._list)
        
    def __getitem__(self,key):
        return self._list[key]

    def shuffle(self):
        random.shuffle(self._list)
"""
Class: Player
Description:
    class manages an instance of player which has a name and a hand
Methods:
    add_won_cards()
    play_a_card()
    isEmpty()
    loseWar()
"""
class Player(object):
    def __init__(self, name):
        self.h = Hand()
        self.n = name

    def __str__(self):
        return self.n

    def add_won_cards(self, card):
        self.h.append(card)

    def play_a_card(self):
        return self.h.pop(0)

    def isEmpty(self):
        if len(self.h) == 0:
            return True
        return False

    def loseWar(self):
        if len(self.h) <= 2:
            return True
        return False

        
class Game(object):
    def __init__(self):
        self.p1 = Player("You")
        self.com = Player("Computer")
        self.D = Deck()
        self.D.shuffle()
        self.pot = Hand()

        
    def game_start(self):
        """
        Function deals 26 cards to each player
        """
        for i in range(26):
            self.p1.add_won_cards(self.D.pop_card())
            self.com.add_won_cards(self.D.pop_card())

        self.p1.h.shuffle()
        self.com.h.shuffle()

    def play_game(self):
        """
        Function to manage gameplay of "War"

        """
        self.p1Card = self.p1.play_a_card()
        self.comCard = self.com.play_a_card()
        print("\n your card\n")
        print(self.p1Card)
        print("\n Computer's Card")
        print(self.comCard)
        self.pot.append(self.p1Card)
        self.pot.append(self.comCard)
        self.p1.h.shuffle()
        self.com.h.shuffle()

        if self.p1Card > self.comCard:
            print("you win the pot")
            for i in range(len(self.pot)):
                self.p1.add_won_cards(self.pot.pop())
            print(len(self.p1.h))

        elif self.comCard > self.p1Card:
            print("computer wins the pot")
            for i in range(len(self.pot)):
                self.com.add_won_cards(self.pot.pop())
            print(len(self.com.h))

        else:
            self.war()

    def war(self):
        """
        function to handle an instance of war encountered
        by the play game function.
        """
        print("this means WAR!")
        while not self.p1Card < self.comCard and not self.comCard < self.p1Card:
            if not self.p1.loseWar() and not self.com.loseWar(): 
                self.p1.h.shuffle()
                self.com.h.shuffle()
                print("Two cards have been placed face down")
                self.p1Card = self.p1.play_a_card()
                self.comCard = self.com.play_a_card()
                self.pot.append(self.p1Card)
                self.pot.append(self.comCard)

                print("Two cards played face up")
                print("Your face up card")
                self.p1Card = self.p1.play_a_card()
                print(self.p1Card)

                print("Opponent's face up card")
                self.comCard = self.com.play_a_card()
                print(self.comCard)



                self.pot.append(self.p1Card)
                self.pot.append(self.comCard)

                if self.p1Card > self.comCard:
                    print("you win the pot")
                    for i in range(len(self.pot)):
                        self.p1.add_won_cards(self.pot.pop())
                    print(len(self.p1.h))

                elif self.comCard > self.p1Card:
                    print("computer wins the pot")
                    for i in range(len(self.pot)):
                        self.com.add_won_cards(self.pot.pop())
                    print(len(self.com.h))

                else:
                    self.war()
            else:
                if self.p1.loseWar():
                    print("you don't have enough cards to continue")
                else:
                    print("Computer doesn't have enough cards to continue")
                break
        
            


    def isOver(self):
        """
        returns true if a player has lost all of their cards
        signaling the end of a game

        """
        if self.p1.isEmpty() or self.com.isEmpty():
            return True
        return False

    def winner(self):
        """
        Prints the name of the game's winner
        """
        
        print("This games winner is, ")
        if not self.p1.isEmpty():
            print(self.p1) 
        else:
            print(self.com)
      


                   





G = Game()
G.game_start()
while not G.isOver():
    G.play_game()
G.winner()




