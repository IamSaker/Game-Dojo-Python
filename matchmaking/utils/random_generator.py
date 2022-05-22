from constants import HABITS, INTRODUCE
from models.gender import Gender
from models.coord import Coord

from random import choice, randint, sample, uniform


class RandomGenerateParameters:
    """ Random generate parameter to Individual instance

    Properties:
        * container: you need to set values in it, see examples below for more details
            - gender_pool: list of Gender
        * non-entity: returns/yields data as function arguments, see examples below for more details
            - AGE_LOWER_BOUND
            - AGE_UPPER_BOUND
            - LNG_LOWER_BOUND
            - LNG_UPPER_BOUND
            - LAT_LOWER_BOUND
            - LAT_UPPER_BOUND

    Methods:
        - random_age
        - random_gender
        - random_intro
        - random_habits
        - random_coord

    Examples:
        >>> generator = RandomGenerateParameters()
        >>> generator.random_gender()
        'FEMALE'
        >>> generator.random_age()
        18
        >>> generator.random_intro()
        '這裡不常開，追我ig'
        >>> generator.random_habits()
        ['旅行', '唱歌', '排球', '睡覺', '聊天', '打屁']
        >>> generator.random_coord()
        Coord(x=-69.80298757935863, y=36.417462727808896)
    """

    AGE_LOWER_BOUND = 18
    AGE_UPPER_BOUND = 100
    LNG_LOWER_BOUND = -180
    LNG_UPPER_BOUND = 180
    LAT_LOWER_BOUND = -90
    LAT_UPPER_BOUND = 90

    def __init__(self) -> None:
        self.gender_pool = Gender.get_all()

    def random_age(self) -> int:
        return randint(self.AGE_LOWER_BOUND, self.AGE_UPPER_BOUND)

    def random_gender(self) -> str:
        return choice(self.gender_pool)

    def random_intro(self) -> str:
        return choice(INTRODUCE)

    def random_habits(self) -> list[str]:
        number = randint(1, len(HABITS))
        return sample(HABITS, k=number)

    def random_coord(self):
        longitude = uniform(self.LNG_LOWER_BOUND, self.LNG_UPPER_BOUND)
        latitude = uniform(self.LAT_LOWER_BOUND, self.LAT_UPPER_BOUND)
        return Coord(longitude, latitude)
