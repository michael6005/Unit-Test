from enum import Enum, IntEnum

class Suit(IntEnum):
    Diamond = 1
    Spade = 2
    Heart = 3
    Club = 4

class Value(IntEnum):
    ace = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13

class Card:
    # A class that describes a card and compares cards by value and suit
    def __init__(self,suit: Suit,value: Value):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value}, {self.suit}'
    
    def __gt__(self, other: Card):     
        if self.value == other.value:
            return self.suit > other.suit
        else:
            self.value > other.value
