import deckofcards
from blackjack_game import get_hand_score
def test_get_hand_score():
    print("-Testing Card values")
    test_cases = [
        ('Spades', '2', 2)
        ('Hearts', '10', 10),
        ('Diamonds', 'J', 10),
        ('Clubs', 'Q', 10),
        ('Spades', 'K', 10),
        ('Hearts', 'A', 11)
    ]
    for suit, rank, expected in test_cases

