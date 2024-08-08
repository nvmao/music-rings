import random

from Ring import Ring
from midi import list_notes_from_midi
from utils import utils


class Game:
    def __init__(self):
        self.notes_dict = list_notes_from_midi("music.mid")
        # for note in self.notes_dict.values():
        #     print(note)

        self.time = 0
        self.minTime = 0
        self.maxTime = 19.8 # duration of the file

        self.angle = 0

        self.rings = []
        radius = 50
        hue = 0
        hueStep = 1 / len(self.notes_dict.values())
        # self.list_notes = self.shuffle_dict(self.list_notes)
        rotateDir = 1
        maxWidth = utils.width / 2
        for note in reversed(self.notes_dict.values()):
            ring = Ring(radius, utils.hueToRGB(hue), self.notes_dict[note['name']], self.maxTime,
                        random.uniform(0, 360), rotateDir)
            rotateDir *= -1
            hue += hueStep
            self.rings.append(ring)
            radius += (maxWidth - 50) / len(self.notes_dict.values())


        # show rings by time
        self.showTimeInterval = 0
        self.showTimeList = {}
        t = 0
        for i in range(len(self.notes_dict)):
            self.showTimeList[i] = t
            if i > 13:
                t += 1
                continue
            t += 3
        self.showTimeList = self.shuffle_dict(self.showTimeList)

    def shuffle_dict(self, d):
        # Convert dictionary items to a list
        items = list(d.items())
        # Shuffle the list of items
        random.shuffle(items)
        # Create a new dictionary from the shuffled list of items
        shuffled_dict = dict(items)
        return shuffled_dict

    def update(self):
        self.showTimeInterval += utils.deltaTime()
        for i, showTime in enumerate(self.showTimeList.values()):
            if showTime < self.showTimeInterval:
                self.rings[i].showTime = True

        self.time += utils.clock.get_time() / 1000.0
        if self.time >= self.maxTime:
            self.time = 0
            for ring in self.rings:
                ring.reset()
        for ring in self.rings:
            ring.update(self.time)

    def draw(self):
        for ring in self.rings:
            ring.draw()