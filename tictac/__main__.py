from tictac.utils import cls
from tictac.tictactoe import (
    TicTacToe,
    play_user,
    play_comp,
    is_there_winner,
    all_the_cells_are_busy,
    is_user_won,
    is_comp_won,
)


def run() -> None:
    game = TicTacToe()
    while True:
        cls()
        print(game)
        play_user(game)
        if is_there_winner(game):
            break
        play_comp(game)
        if is_there_winner(game):
            break
        if all_the_cells_are_busy(game):
            break
    cls()
    print(game)
    if is_user_won(game):
        print("Пользователь выиграл")
    elif is_comp_won(game):
        print("Компьютер выиграл")
    else:
        print("Ничья")


if __name__ == "__main__":
    run()
