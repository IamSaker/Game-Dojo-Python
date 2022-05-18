from constants import HANDS_NUMBER, MAX_USER_NUMBER, ROUNDS_IN_ONE_GAME
from typing import List

from desk import Desk
from player import AiPlayer, HumanPlayer, Player


class ShowDown:
    def __init__(self) -> None:
        self.players: List[Player]
        self.desk = Desk()
        self.rounds: int = ROUNDS_IN_ONE_GAME

    def initial_game(self):
        self._create_players()
        self._shuffle_cards()
        self._draw_card()

    def _create_players(self):
        self._generate_player()
        self._naming()
        self._set_initial_score()

    def _generate_player(self):
        human_number = input('How many people want to join the game? (at most four players):')
    
        self.players = [
            HumanPlayer()
            if i < human_number else AiPlayer()
            for i in range(MAX_USER_NUMBER)
        ]

    def _naming(self):
        for player in self.players:
            player.name_himself()

    def _set_initial_score(self):
        for player in self.players:
            player.point = 0

    def _shuffle_cards(self):
        self.desk.create_standard_desk()
        self.desk.shuffle()

    def _draw_card(self):
        for player in self.players:
            for _ in HANDS_NUMBER:
                player.draw_card(self.desk.cards)

    def play_a_round(self):
        self.rounds -= 1

        compare_cards = [player.show() for player in self.players]
        play_index = self.compare(compare_cards)
        self.add_point(self.players[play_index])

        if not self.rounds:
            self.end_turn()

    def compare(self, cards):
        highest_rank = 0
        highest_suit = 0
        play_index = 0

        for i, card in enumerate(cards):
            if ((card.rank > highest_rank) or
                (card.rank == highest_rank and card.suit > highest_suit)):
                highest_rank, highest_suit = card.rank, card.suit
                play_index = i

        return play_index

    def add_point(self, player):
        point = player.point
        player.point = point + 1

    def end_turn(self):
        player_points = {i: player.point for i, player in enumerate(self.players)}
        maximum = self._get_maximum_points(player_points)
        return self._get_winner(maximum, player_points)

    def _get_maximum_points(self, player_points):
        return max(player_points, key=player_points.values())

    def _get_winner(self, maximum, player_points):
        result = dict(filter(lambda x:x[1] == maximum, player_points.items()))
        index = list(result.keys())[0]
        return self.players[index].name
