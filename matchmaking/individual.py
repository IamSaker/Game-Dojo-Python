from models.coord import Coord
from models.gender import Gender
from models.habits import Habits


class Individual:
    """ Context object whose behavior varies as per its strategy object. """

    def __init__(self) -> None:
        self._id: int
        self._gender: str
        self._age: int
        self._intro: str
        self._habits: Habits
        self._coord: Coord

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int):
        if id <= 0:
            raise ValueError('ID must over than 0')
        self._id = id

    @property
    def gender(self) -> Gender:
        return self._gender

    @gender.setter
    def gender(self, gender: Gender):
        self._gender = gender

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int):
        if age < 18:
            raise ValueError('Age must over than 18')
        self._age = age

    @property
    def intro(self) -> str:
        return self._intro

    @intro.setter
    def intro(self, intro: str):
        if len(intro) > 200:
            raise ValueError('Introduction must be in the 0 character to 200 characters')
        self._intro = intro

    @property
    def habits(self) -> Habits:
        return self._habits

    @habits.setter
    def habits(self, habits: Habits):
        self._habits = habits

    @property
    def coord(self) -> Coord:
        return self._coord

    @coord.setter
    def coord(self, coord: Coord):
        self._coord = coord
