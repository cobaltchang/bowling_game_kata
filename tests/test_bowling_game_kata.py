import os
import sys
import unittest

sys.path.insert(1, os.path.join(
    os.path.dirname(os.path.realpath(__file__)), os.pardir))

from bowling_game_kata import Game  # noqa: E402


class GameTestCase(unittest.TestCase):

    def test_(self):
        pass
