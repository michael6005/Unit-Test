class Card:
# A class that describes a card and compares cards by value and suit
    def __init__(self,suit,value):
        self.value = value
        self.suit = suit
        self.suits_names = ['Diamond','Spade','Heart','Club']
        self.value_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']

    def __repr__(self):
        return '%s : %s' % (self.value_names[self.value], self.suits_names[self.suit])
    def __gt__(self, other):
        # compare values
        if self.value > other.value:
            return True
        if self.value < other.value:
            return False
        # if the values are the same, compare the suits
        if self.suit > other.suit:
            return True
        if self.suit < other.suit:
            return False
