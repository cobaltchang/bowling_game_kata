class Game:
    max_frame = 11

    def __init__(self):
        self.__frame = 0
        self.__frame_end = True
        self.__frame_pins = 0
        self.__score = [0] * self.max_frame
        self.__bonus = 0
        self.__final_pins = 0
        self.__extra_runs = -1

    def roll(self, pins):
        if self.__frame == 10 and self.__frame_end:
            self.score()
            return

        self._set_frame()

        pins = self._normalize_pins(pins)

        self.__frame_pins += pins
        current_score = self.score(pins)

        if self.__frame_pins == 10:
            if self.__frame < (self.max_frame - 1):
                self._set_bonus()
            else:
                self._set_extra_roll(pins)

        print("Frame#%d: roll %s, score:%d" % (self.__frame, ["", "end"][self.__frame_end], current_score))

    def _set_extra_roll(self, pins):
        if self.__extra_runs == -1:
            self.__extra_runs = 1
            self.__frame_end = False

        self.__final_pins += self.__frame_pins
        self.__frame_pins = 0

    def _normalize_pins(self, pins):
        if self.__frame_pins + pins > 10:
            pins = 10 - self.__frame_pins

        return pins

    def _set_frame(self):
        if self.__frame_end:
            self.__frame += 1
            self.__frame_end = False
            self.__frame_pins = 0
        else:
            if self.__extra_runs > 0:
                self.__extra_runs -= 1
            else:
                self.__frame_end = True

    def _set_bonus(self):
        if self.__frame_end:
            self.__bonus = 1
        else:
            self.__bonus = 2
            self._set_frame()

    def score(self, pins=0):
        if self.__bonus > 0:
            self.__score[self.__frame - 1] += pins
            self.__bonus -= 1

        base_score = self.__score[self.__frame - 1] if self.__frame > 0 else 0
        self.__score[self.__frame] = base_score + self.__frame_pins + self.__final_pins

        return self.__score[self.__frame]

    def show_score(self):
        for i in [f + 1 for f in range(self.max_frame) if f < self.__frame]:
            print("Frame#%d: %d" % (i, self.__score[i]))

        if self.__frame == 0:
            print("This is a brand new game, please start rolling.")
        elif self.__frame < self.max_frame:
            print("\nThis game has not been over, continue for your next rolling.")
        else:
            print("\n Game Over!")
