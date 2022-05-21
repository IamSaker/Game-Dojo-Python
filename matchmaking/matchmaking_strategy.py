from base_strategy import MatchmakingStrategy
from constants import POS_INF, NEG_INF
from individual import Individual
from matchmaking_system import gt, lt


class DistanceBasedMatchmakingStrategy(MatchmakingStrategy):
    """ Matchmaking Strategy by Distance-based """

    def matchmaking(self, strategy, myself, individuals) -> Individual:
        the_right_one: str
        matchmaking_distance: int = POS_INF if strategy is lt else NEG_INF

        for individual in individuals:
            if myself.id == individual.id:
                continue

            target_position = individual.coord
            distance = myself.coord.distance(target_position)

            if strategy(distance, matchmaking_distance):
                matchmaking_distance = distance
                the_right_one = individual
            elif is_same(distance, matchmaking_distance):
                the_match_guy = choice_minimum_id(the_right_one, individual)
                the_right_one = the_match_guy

        return the_right_one


class HabitBasedMatchmakingStrategy(MatchmakingStrategy):
    """ Matchmaking Strategy by Habit-based """

    def matchmaking(self, strategy, myself, individuals) -> Individual:
        the_right_one: str
        habit_intersection: list[str] = [] if strategy is gt else list(range(500))

        for individual in individuals:
            if myself.id == individual.id:
                continue

            comparer_habit = individual.habits.get_habit()
            common_interest = myself.habits.find_intersection(comparer_habit)

            if strategy(len(common_interest), len(habit_intersection)):
                habit_intersection = common_interest
                the_right_one = individual
            elif is_same(len(common_interest), len(habit_intersection)):
                the_match_guy = choice_minimum_id(the_right_one, individual)
                the_right_one = the_match_guy

        return the_right_one


def is_same(origin, target) -> bool:
    return origin == target


def choice_minimum_id(origin, target) -> bool:
    return origin if origin.id < target.id else target
