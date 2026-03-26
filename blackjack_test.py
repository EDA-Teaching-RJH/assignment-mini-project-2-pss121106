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
    for suit, rank, expected in test_cases:
        if rank in ['J', 'Q', 'K']:
            c = deckofcards.showcard(suit, rank)
        else:
            c = deckofcards.showcard(suit, rank)
        actual = c.value()
        status = "PASS" if actual == expected else "FAIL"
        print(f"Card: {c},  - Expected: {expected}, - Actual: {actual}, - {status}")
    
    def test_scoring_logic():
        print("- Testing hand scoring -")
        test_hands = [
            ([deckofcards.card('Spades','10'), deckofcards.showcard('Clubs', 'J')], 20),
            ([deckofcards.card('Hearts','A'), deckofcards.card('Diamonds','9')], 20),
            ([deckofcards.card('Hearts','A'), deckofcards.card('Diamonds','A')], 12),
            ([deckofcards.card('Hearts','A'), deckofcards.card('Diamonds','A'), deckofcards.card('Clubs','7')], 13)
            ]
        for hand, expected