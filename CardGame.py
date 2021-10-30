import random
from ProjectPython_misha.DeckOfCards import DeckOfCards
from ProjectPython_misha.Player import Player
from ProjectPython_misha.Card import Card
class CardGame:
# The class that launches the game and determines the winner of the game
    def __init__(self,name1,name2,numbers_cards_for_player=26):
        self.player1=Player(name1,numbers_cards_for_player)
        self.player2=Player(name2,numbers_cards_for_player)
        self.pack_of_cards=DeckOfCards()
    def new_game(self):
        # The method starts a new game shuffles the cards and deals the cards to the players' hands
        self.pack_of_cards.cards_shuffle()
        self.player1.set_hand(self.pack_of_cards)
        self.player2.set_hand(self.pack_of_cards)
    def get_winner(self):
        # The method that determines the winner of the game
        if len(self.player1.cards_of_player) > len(self.player2.cards_of_player):
            return f"The winner of the game: \n{self.player1}"
        if len(self.player1.cards_of_player) < len(self.player2.cards_of_player):
            return f"The winner of the game: \n{self.player2}"
        if len(self.player1.cards_of_player) == len(self.player2.cards_of_player):
            return None

    def __repr__(self):
        return f"{self.player1},{self.player2},{self.pack_of_cards}"





