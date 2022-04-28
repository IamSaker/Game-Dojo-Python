from abc import abstractmethod, ABC
from random import randint
from typing import List

from card import Card


class Player(ABC):
    def __init__(self, name=None, point=None) -> None:
        self._name: str = name
        self._point: int = point
        self._cards: List[Card] = list()

    @abstractmethod
    def show(self):
        NotImplemented

    @abstractmethod
    def draw_card(self, card: Card):
        NotImplemented

    @abstractmethod
    def name_himself(self, name):
        NotImplemented

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, point):
        self._point = point

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, cards):
        self._cards = cards

    def _pick(self, l):
        return randint(0, len(l) - 1)


class AiPlayer(Player):

    def show(self):
        index = self._pick(self._cards)
        return self._cards.pop(index)

    def draw_card(self, cards):
        index = self._pick(cards)
        card = cards.pop(index)
        self._cards.add(card)

    def name_himself(self) -> None:
        self.name = 'AI Player'


class HumanPlayer(Player):

    def show(self):
        for i, card in enumerate(self.cards):
            print(f'Index: {i}, Rank: {card.rank}, Suit: {card.suit}')
        index = input('Choose a card [index]: ')
        return self._cards.pop(int(index))

    def draw_card(self, cards):
        index = self._pick(cards)
        card = cards.pop(index)
        self._cards.append(card)

    def name_himself(self) -> None:
        name = input('Your Name: ')
        self.name = name
