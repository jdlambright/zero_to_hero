
VALUES = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11,
          "Queen": 12, "King": 13, "Ace": 14,}

RANKS = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

SUITS = ("Hearts", "Diamonds", "Spades", "Clubs")


class Card:

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]


    def __str__(self):
        return self.rank + " of " + self.suit
