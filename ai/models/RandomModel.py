from random import Random

import numpy as np

from ai.Model import Model
from ai.Types import Action, GameState
from gomoku_game.Board import Board


class RandomModel(Model):

    def __init__(self, size):
        self.size_x, self.size_y = size
        self.random = Random()

    def train(self, _train_position, _train_correct_move):
        print("Training.")
        print("type _train_position[0]: " + str(type(_train_position[0])))
        print("type _correct_move[0]: " + str(type(_train_correct_move[0])))
        print("Training data: ")
        for data in zip(_train_position, _train_correct_move):
            board, move = data
            print(Board.print_board(board))
            print("Correct move: " + str(move))
        print("End training.")

    def predict(self, game_state) -> Action:
        return Action((self.random.randint(0, self.size_x), self.random.randint(0, self.size_y)))