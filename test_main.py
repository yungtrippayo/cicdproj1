
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


