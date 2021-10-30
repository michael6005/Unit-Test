from ProjectPython_misha.Card1 import Card
import random
from random import randint
from random import shuffle
class DeckOfCards:
# A class that describes a deck of cards
    def __init__(self):
        self.deck_cards=[]
        for suit in range (4):
            for value in range(1,14):
                card=Card(suit,value)
                self.deck_cards.append(card)
    def cards_shuffle(self):
        # Method to shuffle a deck of cards
        random.shuffle(self.deck_cards)

    def deal_one(self):
        # The method draws one random card from the deck. The method will return the card it drew and remove from the deck of cards
        card=random.choice(self.deck_cards)
        self.deck_cards.remove(card)
        return card
    def __repr__(self):
        return f"{self.deck_cards}"
