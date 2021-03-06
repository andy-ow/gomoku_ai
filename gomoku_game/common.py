from enum import Enum, auto

WINNING_NUMBER = 5


class Stone(Enum):
    X = 'X'
    O = 'O'
    EMPTY = '·'

    def __str__(self):
        return self.value


class Player(Enum):
    X = auto()
    O = auto()

    def __init__(self, agent):
        self._agent = agent

    def get_agent(self):
        return self._agent

    def stone(self):
        return Stone.X if self == Player.X else Stone.O

    def opponent(self):
        return Player.O if self == Player.X else Player.X

    def name(self):
        return "Player X" if self == Player.X else "Player O"
