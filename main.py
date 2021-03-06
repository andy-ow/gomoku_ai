import time

from HumanPlayer import HumanPlayer
from Match import Match
from ai.AiPlayer import AiPlayer
from ai.models.RandomModel import RandomModel
from ai.models.SimpleSequentialModel import SimpleSequentialModel
from ai.models.SimpleSequentialModel2 import SimpleSequentialModel2
from gomoku_game import GomokuGame
import tensorflow as tf


def print_stats(stats: dict):
    for player, score in sorted(list(stats.items()), key=lambda z: z[1] / z[0].games_played, reverse=True):
        print(player.get_name, '   ' + str(score) + '/' + str(player.games_played) + '   ', score / player.games_played)


if __name__ == '__main__':
    gpus = tf.config.experimental.list_physical_devices('GPU')
    tf.config.experimental.set_virtual_device_configuration(
        gpus[0], [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=1024)])

    board_size = (9, 9)
    ai_players = []
    for layers_no in [2, 3, 4]:
        for epochs in [10, 30]:
            for max_positions_to_train in [1000]:
                for model in [SimpleSequentialModel]:
                    for after_how_many_to_train in [10, 30]:
                        for kernel_size in [3, 4, 5]:
                            for filters_no in [20, 40]:
                                # ai_player = AiPlayer(name="AI__layers_"+str(layers_no)+"__epochs_"+str(epochs)+"__max_positions_"+str(how_many_games_remember)+"__model_"+str(model.model_name()),
                                ai_player = AiPlayer(name="La" + str(layers_no) + "__e" + str(epochs) + "__max" + str(
                                    max_positions_to_train) + "__a" + str(after_how_many_to_train) + "__" + str(
                                            model.model_name() + "__k"+str(kernel_size) + "__f"+ str(filters_no)),
                                            model=model(board_size, epochs=epochs, layers_no=layers_no, filters_no=filters_no, kernel_size=kernel_size),
                                            shape=(9, 9, 2),
                                            after_how_many_games_to_train=after_how_many_to_train,
                                            max_positions_to_train=max_positions_to_train)
                                ai_players.append(ai_player)
    human_player = HumanPlayer(name="Human")
    random_player = AiPlayer(name="Random", model=RandomModel(size=(9,9)), after_how_many_games_to_train=10000, max_positions_to_train=100, shape=(9,9,2))
    ai_players.append(random_player)
    matches = []
    for player1 in ai_players:
        for player2 in ai_players:
            if player1 != player2:
                match = Match(player1, player2, GomokuGame, board_size)
                matches.append(match)

    rounds = 0
    games = 0
    winner_stats = {}
    for player in ai_players:
        winner_stats[player] = 0
    # a,b = 0,0
    while True:
        for ai_match in matches:
            visible = True if rounds != 0 and rounds % 10 == 0 else False
            """if games%20 ==0:
                b = time.time()
                print("time: " + str(b - a))
                a = time.time()"""
            ai_match.play(visible=visible)
            games += 1
            print("", end=".")
            if games % 100 == 0:
                print()
                print("Games: " + str(games))
                print_stats(winner_stats)
            if ai_match.player1 != ai_match.player2:
                winner_stats[ai_match.winner] += 1
            ai_match.restart()
        rounds += 1
        print()
        print("Games: " + str(games))
        print_stats(winner_stats)
        print("\nRound: " + str(rounds))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
