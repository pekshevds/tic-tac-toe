import random
import enum

type Combination = list[int]
type Combinatios = list[Combination]


class User(enum.Enum):
    USER: str = "X"  # Пользователь
    COMP: str = "O"  # Компьютер
    EMPTY: str = "-"  # Свободная ячейка


class TicTacToe:
    def __init__(self) -> None:
        self._data: list[User] = [
            User.EMPTY,
            User.EMPTY,
            User.EMPTY,
            User.EMPTY,
            User.EMPTY,
            User.EMPTY,
            User.EMPTY,
            User.EMPTY,
            User.EMPTY,
        ]

    @property
    def combinations(self) -> Combinatios:
        return [
            [0, 1, 2],  # horizontal1
            [3, 4, 5],  # horizontal2
            [6, 7, 8],  # horizontal3
            [0, 3, 6],  # vertical1
            [1, 4, 7],  # vertical2
            [2, 5, 8],  # vertical3
            [0, 4, 8],  # diagonal1
            [6, 4, 2],  # diagonal2
        ]

    def get_cell_value(self, cell_index: int) -> User:
        return self._data[cell_index]

    def move(self, cell_index: int, value: User) -> None:
        if 0 > cell_index > 8:
            raise IndexError(f"cell {cell_index} is out of range, use 0-8")
        if self.get_cell_value(cell_index) != User.EMPTY:
            raise ValueError(f"cell {cell_index} is busy")
        self._data[cell_index] = value

    def get_all_free_cells(self) -> list[int]:
        """
        Возвращает индексы всех свободных ячеек"""
        return [i for i, value in enumerate(self._data) if value == User.EMPTY]

    def __str__(self) -> str:
        return f"""
        {f"{0}   {1}   {2}"}
        {f"{self._data[0].value}   {self._data[1].value}   {self._data[2].value}"}
        {f"{3}   {4}   {5}"}
        {f"{self._data[3].value}   {self._data[4].value}   {self._data[5].value}"}
        {f"{6}   {7}   {8}"}
        {f"{self._data[6].value}   {self._data[7].value}   {self._data[8].value}"}"""


def check_line(game: TicTacToe, cell1: int, cell2: int, cell3: int, user: User) -> bool:
    """
    Проверка всели ячейки строки содержат одинаковые значения"""
    return (
        game.get_cell_value(cell1)
        == game.get_cell_value(cell2)
        == game.get_cell_value(cell3)
        == user
    )


def check_who_won(game: TicTacToe, user: User) -> bool:
    """
    Определяет победу игрока (пользователь или компьютер)"""
    return any(
        [
            check_line(game, line[0], line[1], line[2], user)
            for line in game.combinations
        ]
    )


def user_won(game: TicTacToe) -> bool:
    """
    Определяет победу пользователя"""
    return check_who_won(game, User.USER)


def comp_won(game: TicTacToe) -> bool:
    """
    Определяет победу компьютера"""
    return check_who_won(game, User.COMP)


def get_free_random_index(game: TicTacToe) -> int:
    """
    Вохвращает индекс свободной случайноя ячейки"""
    return random.choice(game.get_all_free_cells())


def play_user(game: TicTacToe) -> None:
    game.move(
        int(input(f"Введите индекс ячейки {game.get_all_free_cells()}: ")),
        User.USER,
    )


def play_comp(game: TicTacToe) -> None:
    game.move(get_free_random_index(game), User.COMP)


def is_there_winner(game: TicTacToe) -> bool:
    return user_won(game) or comp_won(game)


def is_user_won(game: TicTacToe) -> bool:
    return user_won(game)


def is_comp_won(game: TicTacToe) -> bool:
    return comp_won(game)


def all_the_cells_are_busy(game: TicTacToe) -> bool:
    return len(game.get_all_free_cells()) == 0


__all__ = (
    "TicTacToe",
    "play_user",
    "play_comp",
    "is_there_winner",
    "all_the_cells_are_busy",
    "is_user_won",
    "is_comp_won",
)
