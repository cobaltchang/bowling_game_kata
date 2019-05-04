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

    def _roll_spare(self):
        self.game.roll(4)
        self.game.roll(6)

    def test_roll_all_zeros(self):
        self._roll_many(0, 20)

        self.assertEqual(self.game.score(), 0)

    def test_roll_all_ones(self):
        self._roll_many(1, 20)

        self.assertEqual(self.game.score(), 20)

    def test_roll_one_spare(self):
        self._roll_spare()
        self.game.roll(3)
        self._roll_many(0, 17)

        self.assertEqual(self.game.score(), 16)

    def test_roll_one_strike(self):
        self.game.roll(10)
        self.game.roll(2)
        self.game.roll(4)
        self._roll_many(0, 16)

        self.assertEqual(self.game.score(), 22)
