from card import Card
import random


class Deck(Card):

    def __init__(self,rank, suit):
        super().__init__(self, rank, suit)

        self.all_cards = []

        for suit in SUITS:
            for rank in RANKS:
                #create teh card object
                created_card = Card(rank,suit)
                self.all_cards.append(created_card)


    def shuffle(self):

        random.shuffle(self.all_cards)


    def deal_one(self):
        return self.all_cards.pop()

