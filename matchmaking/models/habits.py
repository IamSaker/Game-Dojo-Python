class Habits:
    """ Habit related

    Methods:
        - get_habit
        - add_habit
        - find_intersection

    Examples:
        >>> habits = Habits()
        >>> habits.add_habit(some_habit)
        >>> my_habits = habits.get_habit()
        >>> habits.find_intersection(other_habits)
    """

    def __init__(self) -> None:
        self._habits: list[str] = []

    def get_habit(self) -> list[str]:
        return self._habits

    def add_habit(self, habit: str) -> None:
        if not isinstance(habit, str):
            raise TypeError('Habit must be string')
        if len(habit) > 10 and len(habit) <= 0:
            raise ValueError('Habit must be in the 0 character to 10 characters')
        self._habits.append(habit)

    def find_intersection(self, other_habits) -> list[str]:
        return list(set(self._habits).intersection(set(other_habits)))
