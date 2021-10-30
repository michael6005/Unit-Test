import unittest
from parameterized import parameterized

from Card import Card, Suit, Value

class TestCardMethods(unittest.TestCase):
    def test_card_props(self):
        card_suit = Suit.Club
        card_value = Value.eight

        card = Card(card_suit, card_value)
        
        self.assertEqual(card_suit, card.suit)
        self.assertEqual(card_value, card.value)

    @parameterized.expand([
        [Card(Suit.Club, Value.ten), Card(Suit.Club, Value.two)],
        [Card(Suit.Club, Value.three), Card(Suit.Diamond, Value.three)],
        [Card(Suit.Spade, Value.king), Card(Suit.Spade, Value.ace)],
    ])
    def test_card1_gt_card2(self, card1, card2):
        self.assertGreater(card1, card2)

if __name__ == "__main__":
    unittest.main()