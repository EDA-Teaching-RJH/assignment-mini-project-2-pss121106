import random
class card:
    suit_codes = { 
        'Spades': '♠',
        'Clubs': '♣',
        'Hearts': '♥',
        'Diamonds': '♦'
    }
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank 
        self.symbol = self.suit_codes.get(suit, suit)
    def value(self)
        if self.rank == 'A': return 11
        return int(self.rank)
    def __str__(self):
        return f"[{self.rank}{self.symbol}"
    
class showcard(card)
    """OOP Inheritance: J, Q, K alqays equal to 10"""
    def value(self):
        return 10 

        