class Game:

    def __init__(self):
        self._scores = []

    def roll(self, pins):
        self._scores.append(pins)

    def score(self):
        score = 0
        for i in range(len(self._scores)):
            score += self._scores[i]

        return score
