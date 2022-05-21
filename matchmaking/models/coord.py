from dataclasses import dataclass

from math import sqrt


@dataclass
class Coord:
    x: float = 0.0
    y: float = 0.0

    def distance(self, newpostion):
        return sqrt((newpostion.x - self.x)**2 + (newpostion.y - self.y)**2)
