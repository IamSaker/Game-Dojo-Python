from enum import Enum, auto


class Gender(Enum):
    MALE = auto()
    FEMALE = auto()

    def get_all() -> list:
        return Gender._member_names_
