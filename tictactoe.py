import random
import enum


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
        self._combinations: list[list[int]] = [
            [0, 1, 2],  # horizontal1
            [3, 4, 5],  # horizontal2
            [6, 7, 8],  # horizontal3
            [0, 3, 6],  # vertical1
            [1, 4, 7],  # vertical2
            [2, 5, 8],  # vertical3
            [0, 4, 8],  # diagonal1
            [6, 4, 2],  # diagonal2
        ]

    def __str__(self) -> str:
        return f"""
        {f"{0}   {1}   {2}"}
        {f"{self._data[0].value}   {self._data[1].value}   {self._data[2].value}"}
        {f"{3}   {4}   {5}"}
        {f"{self._data[3].value}   {self._data[4].value}   {self._data[5].value}"}
        {f"{6}   {7}   {8}"}
        {f"{self._data[6].value}   {self._data[7].value}   {self._data[8].value}"}"""

    def _check_line(self, cell1: int, cell2: int, cell3: int, user: User) -> bool:
        """
        Проверка всели ячейки строки содержат одинаковые значения"""
        return self._data[cell1] == self._data[cell2] == self._data[cell3] == user

    def _check_who_won(self, user: User) -> bool:
        """
        Определяет победу игрока (пользователь или компьютер)"""
        return any(
            [
                self._check_line(line[0], line[1], line[2], user)
                for line in self._combinations
            ]
        )

    def _user_won(self) -> bool:
        """
        Определяет победу пользователя"""
        return self._check_who_won(User.USER)

    def _comp_won(self) -> bool:
        """
        Определяет победу компьютера"""
        return self._check_who_won(User.COMP)

    def _set_value(self, cell: int, value: User) -> None:
        """
        Занимает ячейку (Пишет Х или О)"""
        if 0 > cell > 8:
            raise IndexError(f"cell {cell} is out of range, use 0-8")
        if self._data[cell] != User.EMPTY:
            raise ValueError(f"cell {cell} is busy")
        self._data[cell] = value

    def _get_all_free_cells(self) -> list[int]:
        """
        Возвращает индексы всех свободных ячеек"""
        return [i for i, value in enumerate(self._data) if value == User.EMPTY]

    def _get_free_random_index(self) -> int:
        """
        Вохвращает индекс свободной случайноя ячейки"""
        return random.choice(self._get_all_free_cells())

    def play_user(self) -> None:
        self._set_value(
            int(input(f"Введите индекс ячейки {self._get_all_free_cells()}: ")),
            User.USER,
        )

    def play_comp(self) -> None:
        self._set_value(self._get_free_random_index(), User.COMP)

    def is_there_winner(self) -> bool:
        return self._user_won() or self._comp_won()

    def is_user_won(self) -> bool:
        return self._user_won()

    def is_comp_won(self) -> bool:
        return self._comp_won()

    def all_the_cells_are_busy(self) -> bool:
        return len(self._get_all_free_cells()) == 0


__all__ = ("TicTacToe",)
