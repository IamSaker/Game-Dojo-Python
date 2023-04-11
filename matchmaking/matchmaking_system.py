from individual import Individual
from base_strategy import MatchmakingStrategy


class MatchmakingSystem:
    """ In dating apps, matchmaking is the process of attracting each other for online dating.

    Properties:
        * container: you need to set values in it, see examples below for more details
            - individuals: candidate of dating app to you could be interest
            - strategies: matchmaking strategy
            - matchers: find you have feelings for someone 

    Methods:
        - launch
        - match
        - snow_all_match

    Examples:
        >>> matchmaking_system = MatchmakingSystem(people, strategies)
        >>> matchmaking_system.launch()
        >>> matchmaking_system.snow_all_match()
        User id: 100:
            Match by distance is user id: 58
            And match by habit is user id: 13
    """

    def __init__(self, individuals, strategies) -> None:
        self.strategies: list[MatchmakingStrategy] = strategies
        self.individuals: list[Individual] = individuals
        self.matchers: list[tuple] = []

    def launch(self):
        for protagonist in self.individuals:
            self.match(protagonist)

    def match(self, protagonist):
        distance_based = self.strategies[0]
        habit_based = self.strategies[1]
        match_by_distance = distance_based.matchmaking(lt, protagonist, self.individuals)
        match_by_habit = habit_based.matchmaking(gt, protagonist, self.individuals)
        self.matchers.append((protagonist.id, match_by_distance.id, match_by_habit.id))

    def snow_all_match(self):
        for matcher in self.matchers:
            print(f'''User id: {matcher[0]}:
            Match by distance is user id: {matcher[1]}
            And match by habit is user id: {matcher[2]}\n''')


def gt(o, t) -> bool:
    return o > t


def lt(o, t) -> bool:
    return o < t
