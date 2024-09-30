import pytest
from tictac.tictactoe import (
    TicTacToe,
    User,
    is_there_winner,
    all_the_cells_are_busy,
    is_user_won,
    is_comp_won,
    get_free_random_index,
)


@pytest.fixture
def game() -> TicTacToe:
    return TicTacToe()


@pytest.fixture
def full_game() -> TicTacToe:
    game = TicTacToe()
    game.move(0, User.USER)
    game.move(1, User.COMP)
    game.move(2, User.COMP)
    game.move(3, User.USER)
    game.move(4, User.USER)
    game.move(5, User.USER)
    game.move(6, User.USER)
    game.move(7, User.COMP)
    game.move(8, User.COMP)
    return game


@pytest.fixture
def user() -> User:
    return User.USER


@pytest.fixture
def comp() -> User:
    return User.COMP


@pytest.fixture
def computers_game() -> TicTacToe:
    game = TicTacToe()
    game.move(0, User.COMP)
    game.move(1, User.COMP)
    game.move(2, User.COMP)
    return game


@pytest.fixture
def user_game() -> TicTacToe:
    game = TicTacToe()
    game.move(0, User.USER)
    game.move(1, User.USER)
    game.move(2, User.USER)
    return game


def test__is_there_winner__check_computey_is_winner(computers_game: TicTacToe):
    assert is_there_winner(computers_game) is True


def test__is_there_winner__check_user_is_winner(user_game: TicTacToe):
    assert is_there_winner(user_game) is True


def test__is_there_winner__check_move_cell_index_out_of_range_0_7(game: TicTacToe):
    with pytest.raises(IndexError):
        game.move(9, User.USER)


def test__is_there_winner__check_move_cell_index_already_busy(game: TicTacToe):
    game.move(0, User.USER)
    with pytest.raises(ValueError):
        game.move(0, User.USER)


def test__is_there_winner__check_move_success(game: TicTacToe):
    game.move(0, User.USER)
    assert game.get_cell_value(0) == User.USER


def test__get_all_free_cells__check_all_cells_are_empty(game: TicTacToe):
    assert game.get_all_free_cells() == TicTacToe().get_all_free_cells()


def test__get_all_free_cells__check_all_cells_are_full(full_game: TicTacToe):
    assert len(full_game.get_all_free_cells()) == 0


def test__get_all_free_cells__check_some_cells_are_full(full_game: TicTacToe):
    assert len(full_game.get_all_free_cells()) != 9


def test__all_the_cells_are_busy__check_all_cells_are_full(full_game: TicTacToe):
    assert all_the_cells_are_busy(full_game) is True


def test__all_the_cells_are_busy__check_all_cells_are_empty(game: TicTacToe):
    assert all_the_cells_are_busy(game) is False


def test__is_user_won__check_is_it_true(game: TicTacToe):
    game.move(0, User.USER)
    game.move(1, User.USER)
    game.move(2, User.USER)
    assert is_user_won(game) is True


def test__is_user_won__check_is_it_false(game: TicTacToe):
    game.move(0, User.USER)
    game.move(1, User.USER)
    game.move(2, User.COMP)
    assert is_user_won(game) is False


def test__is_comp_won__check_is_it_true(game: TicTacToe):
    game.move(0, User.COMP)
    game.move(1, User.COMP)
    game.move(2, User.COMP)
    assert is_comp_won(game) is True


def test__is_comp_won__check_is_it_false(game: TicTacToe):
    game.move(0, User.USER)
    game.move(1, User.COMP)
    game.move(2, User.COMP)
    assert is_comp_won(game) is False


def test__get_free_random_index__check_if_the_game_is_full(full_game: TicTacToe):
    with pytest.raises(IndexError):
        get_free_random_index(full_game)


def test__get_free_random_index__check_if_the_game_is_not_full(game: TicTacToe):
    assert get_free_random_index(game) is not None
