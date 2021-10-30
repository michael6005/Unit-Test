class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.suits = {1:"Diamond",2:"Spade",3:"Heart",4:"Club"}
    def __gt__(self, other):
        if self.value > other.value:
            return True
        elif self.value == other.value and self.suit > other.suit:
            return True
        else:
            return False
    def __repr__(self):
        return f"{self.value},{self.suits[self.suit]}"
#if __name__=="main":
# Card1=Card(13,4)
# Card2=Card(13,1)
# print(Card1<Card2)
# print(Card1==Card2)
# print(Card1>Card2)
# suits={"Diamond":1,"Spade":2,"Heart":3,"Club":4}