from player import Player


class ExchangeHands:
    def __init__(self, origin_player) -> None:
        self.is_used: bool = False
        self.rounds: int = 3
        self.origin_player: Player = origin_player
        self.target_player: Player = None

    def execute(self):
        if self.is_used:
            print('Exchange hands could only be used once!')
            return
        self.choose_player()
        self.exchange()

    def _validate(self, player):
        return self.origin_player == player

    def choose_player(self, player):
        if self._validate():
            print("Can't exchange with yourself!")
        self.target_player = player

    def exchange(self):
        self.origin_player._cards, self.target_player._cards = self.target_player._cards, self.origin_player._cards

    def exchange_back(self):
        self.timer()
        if not self.rounds:
            self.exchange()

    def timer(self):
        self.rounds -= 1
