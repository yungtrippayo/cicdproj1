
import pytest
from unittest.mock import patch

from main import TicTacToe


def test_init():
    game = TicTacToe()
    assert game.board == [' '] * 9
    assert game.current_player == 'X'


