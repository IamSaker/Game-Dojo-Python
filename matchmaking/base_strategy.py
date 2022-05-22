from abc import ABC, abstractmethod
from individual import Individual


class MatchmakingStrategy(ABC):
    """ Matchmaking Criteria Interface """

    @abstractmethod
    def matchmaking(self, strategy, myself, individuals) -> Individual:
        """ matchmaking strategy

        Args:
            strategy : strategy you want to execute
            myself (Individual) : matchmaking on an individual basis
            individuals (List[Individual]) : all users can matchmaking

        Returns:
            individual (Individual): individual instance
        """
        return NotImplemented
