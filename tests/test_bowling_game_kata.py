import os
import sys
import unittest

sys.path.insert(1, os.path.join(
    os.path.dirname(os.path.realpath(__file__)), os.pardir))

from bowling_game_kata import Game  # noqa: E402


class GameTestCase(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def _roll_many(self, pins, times):
        for i in range(times):
            self.game.roll(pins)

    def test_roll_all_zeros(self):
        self._roll_many(0, 20)

        self.assertEqual(self.game.score(), 0)

    def test_roll_all_ones(self):
        self._roll_many(1, 20)

        self.assertEqual(self.game.score(), 20)
