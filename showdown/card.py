import enum


class Rank(enum.IntEnum):
    TWO = enum.auto()
    THREE = enum.auto()
    FOUR = enum.auto()
    FIVE = enum.auto()
    SIX = enum.auto()
    SEVEN = enum.auto()
    EIGHT = enum.auto()
    NINE = enum.auto()
    TEN = enum.auto()
    JACK = enum.auto()
    QUEEN = enum.auto()
    KING = enum.auto()
    ACE = enum.auto()


class Suit(enum.IntEnum):
    CLUB = enum.auto()
    DIAMOND = enum.auto()
    HEART = enum.auto()
    SPADE = enum.auto()


class Card:
    def __init__(self, rank, suit) -> None:
        self.rank: Rank = rank
        self.suit: Suit = suit
