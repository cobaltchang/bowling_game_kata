import os
import sys
import unittest

sys.path.insert(1, os.path.join(
    os.path.dirname(os.path.realpath(__file__)), os.pardir))

from bowling_game_kata import Game  # noqa: E402


class GameTestCase(unittest.TestCase):

    def test_roll_all_zeros(self):
        game = Game()
        for i in range(20):
            game.roll(0)

        self.assertEqual(game.score(), 0)
