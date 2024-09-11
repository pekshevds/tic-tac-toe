import random
from utils import cls
from tictactoe import TicTacToe, User


def show_play_table(game: TicTacToe) -> None:
    cls()
    print(game)


def play_user(game: TicTacToe) -> None:
    cell = 9
    while cell not in game.all_free_cells():
        show_play_table(game)
        cell = int(input("input cell index: "))
    game.play(cell, User.USER)


def play_comp(game: TicTacToe) -> None:
    cell = random.choice(game.all_free_cells())
    game.play(cell, User.COMP)


def show_result(game: TicTacToe) -> None:
    show_play_table(game)
    if game.is_user_won():
        print("Пользователь выиграл")
    elif game.is_comp_won():
        print("Компьютер выиграл")
    else:
        print("Ничья")


def run() -> None:
    game = TicTacToe()
    while True:
        # Играет пользователь
        play_user(game)
        if game.is_there_winner():
            break
        # Играет компьютер
        play_comp(game)
        if game.is_there_winner():
            break
        # Проверка наличия пустых ячеек (все заполнены - ничья)
        if game.all_the_cells_are_busy():
            break
    # Вывод результатов игры
    show_result(game)


if __name__ == "__main__":
    run()
