from ProjectPython_misha.DeckOfCards import DeckOfCards
from ProjectPython_misha.Player import Player
from ProjectPython_misha.Card1 import Card
from ProjectPython_misha.CardGame import CardGame
# name_player1=input("Enter the of player 1: ")  #выкинуть из ораот
# name_player2=input("Enter the of player 2: ")   #выкинуть из ораот
# Game1=CardGame(name_player1,name_player2,26)   #выкинуть из ораот
Game1=CardGame("Michael","Lidor",26)
Game1.new_game()
print(Game1.player1)
print(Game1.player2)
for i in range(10):
    card_player1=Game1.player1.get_card()
    Game1.player1.cards_of_player.remove(card_player1)
    card_player2=Game1.player2.get_card()
    Game1.player2.cards_of_player.remove(card_player2)
    print(card_player1)
    print(card_player2)
    if card_player1 > card_player2:
        Game1.player1.add_card(card_player2)
        Game1.player1.add_card(card_player1)
        print(f"Michael is winner")
    else: Game1.player2.add_card(card_player1),Game1.player2.add_card(card_player2),print(f"Lidor is winner")
    print(len(Game1.player1.cards_of_player)) #Можно удалять
    print(len(Game1.player2.cards_of_player)) #Можно удалять
    print(Game1.player1)  #Можно удалять
    print(Game1.player2)   #Можно удалять
print(Game1.get_winner())
