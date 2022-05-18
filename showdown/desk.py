from random import shuffle
from typing import List

from card import Card, Rank, Suit


class Desk:
    def __init__(self) -> None:
        self.cards: List[Card] = list()

    def shuffle(self):
        shuffle(self.cards)

    def create_standard_desk(self):
        for suit in Suit:
            for rank in Rank:
                self.cards.append(Card(rank, suit))
