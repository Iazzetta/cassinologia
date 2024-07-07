from dataclasses import dataclass


@dataclass
class Player:
    coins: float
    ganhos: float

    def add_ganho(self, value: float):
        self.ganhos += value
