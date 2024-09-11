from utils import cls
from tictactoe import TicTacToe


def run() -> None:
    game = TicTacToe()
    while True:
        cls()
        print(game)
        game.play_user()
        if game.is_there_winner():
            break
        game.play_comp()
        if game.is_there_winner():
            break
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
