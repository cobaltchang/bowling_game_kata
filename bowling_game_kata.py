class Game:

    def __init__(self):
        self._scores = []

    def roll(self, pins):
        self._scores.append(pins)

    def score(self):
        score = 0
        roll_index = 0
        for frame in range(10):
            score += self._scores[roll_index] + self._scores[roll_index + 1]
            roll_index += 2

        return score
