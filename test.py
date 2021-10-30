import unittest

from Card import Card, Suit, Value

class TestCardMethods(unittest.TestCase):
    def test_card_props(self):
        card_suit = Suit.Club
        card_value = Value.eight
        card = Card(card_suit, card_value)
        
        self.assertEqual(card.suit, card_suit)
        self.assertEqual(card.value, card_value)

    # def test_card_ranking(self):
    #     card = Card(Suit)

if __name__ == "__main__":
    unittest.main()