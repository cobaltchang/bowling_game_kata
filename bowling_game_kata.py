class Game:

    def __init__(self):
        self._scores = []

    def roll(self, pins):
        self._scores.append(pins)

    def score(self):
        score = 0
        roll_index = 0
        for frame in range(10):
            if self._scores[roll_index] == 10:
                score += 10 + self._scores[roll_index + 1] + self._scores[roll_index + 2]
                roll_index += 1
            elif self._is_spare(roll_index):
                score += 10 + self._scores[roll_index + 2]
                roll_index += 2
            else:
                score += self._scores[roll_index] + self._scores[roll_index + 1]
                roll_index += 2

        return score

    def _is_spare(self, roll_index):
        return (self._scores[roll_index] + self._scores[roll_index + 1]) == 10
