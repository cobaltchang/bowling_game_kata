class Game:

    def __init__(self):
        self._scores = []

    def roll(self, pins):
        self._scores.append(pins)

    def score(self):
        score = 0
        roll_index = 0
        for frame in range(10):
            if self._is_strike(roll_index):
                score += 10 + self._strike_bonus(roll_index)
                roll_index += 1
            elif self._is_spare(roll_index):
                score += 10 + self._spare_bonus(roll_index)
                roll_index += 2
            else:
                score += self._sum_of_rolls_in_frame(roll_index)
                roll_index += 2

        return score

    def _is_strike(self, roll_index):
        return self._scores[roll_index] == 10

    def _is_spare(self, roll_index):
        return (self._scores[roll_index] + self._scores[roll_index + 1]) == 10

    def _sum_of_rolls_in_frame(self, roll_index):
        return self._scores[roll_index] + self._scores[roll_index + 1]

    def _strike_bonus(self, roll_index):
        return self._scores[roll_index + 1] + self._scores[roll_index + 2]

    def _spare_bonus(self, roll_index):
        return self._scores[roll_index + 2]
