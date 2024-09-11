import tictactoe


class TestTicTacToe:
    def test__check_line_comp(self) -> None:
        self.game = tictactoe.TicTacToe()
        user = tictactoe.User.COMP
        for line in self.game._combinations:
            self.game._data[line[0]] = user
            self.game._data[line[1]] = user
            self.game._data[line[2]] = user
            assert self.game._check_line(line[0], line[1], line[2], user) is True

    def test__check_line_user(self) -> None:
        self.game = tictactoe.TicTacToe()
        user = tictactoe.User.USER
        for line in self.game._combinations:
            self.game._data[line[0]] = user
            self.game._data[line[1]] = user
            self.game._data[line[2]] = user
            assert self.game._check_line(line[0], line[1], line[2], user) is True

    def test__user_won_positive(self) -> None:
        self.game = tictactoe.TicTacToe()
        user = tictactoe.User.USER
        self.game._data[0] = user
        self.game._data[1] = user
        self.game._data[2] = user
        assert self.game._user_won() is True

    def test__user_won_negative(self) -> None:
        self.game = tictactoe.TicTacToe()
        user = tictactoe.User.USER
        self.game._data[0] = user
        self.game._data[1] = tictactoe.User.COMP
        self.game._data[2] = user
        assert self.game._user_won() is not True

    def test__comp_won_positive(self) -> None:
        self.game = tictactoe.TicTacToe()
        user = tictactoe.User.COMP
        self.game._data[0] = user
        self.game._data[1] = user
        self.game._data[2] = user
        assert self.game._comp_won() is True

    def test__comp_won_negative(self) -> None:
        self.game = tictactoe.TicTacToe()
        user = tictactoe.User.COMP
        self.game._data[0] = user
        self.game._data[1] = tictactoe.User.USER
        self.game._data[2] = user
        assert self.game._comp_won() is not True

    def test_all_free_cells(self) -> None:
        self.game = tictactoe.TicTacToe()
        self.game._data[0] = tictactoe.User.USER
        assert len(self.game.all_free_cells()) == 8

    def test_is_there_winner(self) -> None:
        self.game = tictactoe.TicTacToe()
        user = tictactoe.User.COMP
        self.game._data[0] = user
        self.game._data[1] = user
        self.game._data[2] = user
        assert self.game.is_there_winner() is True

    def test_is_user_won(self) -> None:
        self.game = tictactoe.TicTacToe()
        user = tictactoe.User.USER
        self.game._data[0] = user
        self.game._data[1] = user
        self.game._data[2] = user
        assert self.game.is_there_winner() is True

    def test_is_comp_won(self) -> None:
        self.game = tictactoe.TicTacToe()
        user = tictactoe.User.COMP
        self.game._data[0] = user
        self.game._data[1] = user
        self.game._data[2] = user
        assert self.game.is_there_winner() is True

    def test_all_the_cells_are_busy_positive(self) -> None:
        self.game = tictactoe.TicTacToe()
        self.game._data = [
            tictactoe.User.USER,
            tictactoe.User.USER,
            tictactoe.User.USER,
            tictactoe.User.USER,
            tictactoe.User.USER,
            tictactoe.User.USER,
            tictactoe.User.USER,
            tictactoe.User.USER,
            tictactoe.User.USER,
        ]
        assert self.game.all_the_cells_are_busy() is True

    def test_all_the_cells_are_busy_negative(self) -> None:
        self.game = tictactoe.TicTacToe()
        self.game._data = [
            tictactoe.User.EMPTY,
            tictactoe.User.USER,
            tictactoe.User.USER,
            tictactoe.User.USER,
            tictactoe.User.USER,
            tictactoe.User.USER,
            tictactoe.User.USER,
            tictactoe.User.USER,
            tictactoe.User.USER,
        ]
        assert self.game.all_the_cells_are_busy() is not True
