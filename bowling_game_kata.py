class Game:

    def __init__(self):
        self._scores = [0] * 21
        self._index = 0

    def roll(self, pins):
        self._scores[self._index] = pins
        self._index += 1

    def score(self):
        score = 0
        for i in range(len(self._scores)):
            score += self._scores[i]

        return score
