from abc import ABC, abstractmethod
from typing import List, Tuple

from Agent import Agent
from ai.Types import Action, GameState


class Game(ABC):

    @abstractmethod
    def __init__(self, players: List[Agent]):
        raise TypeError("TypeError: This is an Abstract Class and it cannot be instantiated")

    @abstractmethod
    def make_move(self, action: Action):
        pass

    @abstractmethod
    def is_playing(self) -> bool:
        pass

    @abstractmethod
    def get_current_player(self) -> Agent:
        pass

    @abstractmethod
    def get_history_of_winning_moves(self) -> List[Tuple[GameState, Action]]:
        pass

    @abstractmethod
    def print_game(self):
        pass

