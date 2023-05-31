
import pytest
from unittest.mock import patch

from main import TicTacToe


def test_init():
    game = TicTacToe()
    assert game.board == [' '] * 9
    assert game.current_player == 'X'


def test_print_board(capsys):
    game = TicTacToe()
    game.print_board()
    captured = capsys.readouterr()
    assert captured.out == '  |   |  \n---------\n  |   |  \n---------\n  |   |  \n'


@pytest.mark.parametrize("board, result", [
    (['X', 'X', 'X',
      ' ', ' ', ' ',
      ' ', ' ', ' '], 'X'),
    (['O', 'O', 'O',
      ' ', ' ', ' ',
      ' ', ' ', ' '], 'O'),
    (['X', ' ', ' ',
      'X', ' ', ' ',
      'X', ' ', ' '], 'X'),
    (['O', ' ', ' ',
      'O', ' ', ' ',
      'O', ' ', ' '], 'O'),
    (['X', ' ', ' ',
      ' ', 'X', ' ',
      ' ', ' ', 'X'], 'X'),
    ([' ', ' ', 'O',
      ' ', 'O', ' ',
      'O', ' ', ' '], 'O'),
    ([' ', ' ', ' ',
      ' ', ' ', ' ',
      ' ', ' ', ' '], False),
    (['X', 'O', 'X',
      'X', 'O', 'X',
      'O', 'X', 'O'], 'Draw'),
])
def test_check_win(board, result):
    game = TicTacToe()
    game.board = board
    assert game.check_win() == result


@patch('builtins.input', return_value='5')
def test_get_move(input):
    game = TicTacToe()
    assert game.get_move() == 4


if __name__ == '__main__':
    pytest.main(['--html=report.html'])
