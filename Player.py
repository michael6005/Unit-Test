from ProjectPython_misha.Card1 import Card
from ProjectPython_misha.DeckOfCards import DeckOfCards
import random
class Player:
# class describes the actions of one player in the game
    def __init__(self,name,numbers_cards_for_player=26):
        self.name=name
        self.numbers_cards_for_player=numbers_cards_for_player
        self.cards_of_player=[]

    def __str__(self):
        return f"{self.name}:,{self.cards_of_player}"

    def set_hand(self,deck_of_cards:DeckOfCards):
        # The method distributes cards from the deck of cards to the hands of the players
       for i in range(self.numbers_cards_for_player):
            self.cards_of_player.append(deck_of_cards.deal_one())

    def get_card(self):
        # Method throws a card from the player's hand
        random_card=random.choice(self.cards_of_player)
        return random_card

    def add_card(self,card):
        # The method adds the card that the players discarded to the hands of the winning player
        self.cards_of_player.append(card)

    def __repr__(self):
        return f"{self.name}:,{self.cards_of_player}"


