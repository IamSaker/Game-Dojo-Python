from constants import BASE
from individual import Individual
from matchmaking_strategy import DistanceBasedMatchmakingStrategy, HabitBasedMatchmakingStrategy
from matchmaking_system import MatchmakingSystem
from models.habits import Habits
from utils.random_generator import RandomGenerateParameters


def main():
    people: list = []
    for identity in range(1, BASE+1):
        people.append(create(identity))
    
    strategies = [
        DistanceBasedMatchmakingStrategy(),
        HabitBasedMatchmakingStrategy()
    ]

    matchmaking_system = MatchmakingSystem(
        people,
        strategies
    )
    matchmaking_system.launch()
    matchmaking_system.snow_all_match()


def create(identity):
    generator = RandomGenerateParameters()

    individual = Individual()
    individual.id = identity
    individual.gender = generator.random_gender()
    individual.age = generator.random_age()
    individual.intro = generator.random_intro()
    individual.coord = generator.random_coord()

    habits = Habits()
    for habit in generator.random_habits():
        habits.add_habit(habit)
    individual.habits = habits

    return individual


if __name__ == '__main__':
    main()
