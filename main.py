import random
from utils import cls
from tictactoe import TicTacToe, User


def run() -> None:
    game = TicTacToe()
    while True:
        cls()
        print(game)

        # Играет пользователь
        game.play(int(input("input cell index: ")), User.USER)
        if game.is_there_winner():
            break
        # Играет компьютер
        cell = random.choice(game.all_free_cells())
        game.play(cell, User.COMP)
        # Проверка наличия победителя
        if game.is_there_winner():
            break
        # Проверка наличия пустых ячеек (все заполнены - ничья)
        if game.all_the_cells_are_busy():
            break
    cls()
    print(game)
    if game.is_user_won():
        print("Пользователь выиграл")
    elif game.is_comp_won():
        print("Компьютер выиграл")
    else:
        print("Ничья")


if __name__ == "__main__":
    run()
