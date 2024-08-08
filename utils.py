import colorsys

import pygame
import math

from Box2D import b2World
from pygame.locals import *

from pygame import Vector2, mixer, time
import pygame.midi


# a global class
# store global variables, functions

class Utils():

    def __init__(self):

        pygame.init()

        self.width = 1280
        self.height = 1280

        self.screen = pygame.display.set_mode((self.width, self.height), DOUBLEBUF, 16)
        self.dt = 0
        self.clock = pygame.time.Clock()

        #midi player
        pygame.midi.init()
        self.volumeScale = 10
        self.midiPlayer = pygame.midi.Output(0)


    def initDeltaTime(self):  # calculate deltaTime
        t = self.clock.tick(60)
        self.dt = t / 1000

    def deltaTime(self):
        return self.dt


    def distance(self, x1, y1, x2, y2):
        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0)

    def hueToRGB(self,hue):
        # Convert HSV to RGB
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        # Scale RGB values to 0-255 range
        return (int(r * 255), int(g * 255), int(b * 255))

    # map value x from range1 to range2
    def map_value(self,x, minRange1, maxRange1, minRange2, maxRange2):
        if minRange1 == maxRange1:
            raise ValueError("minRange1 and maxRange1 cannot be equal.")
        normalized_x = (x - minRange1) / (maxRange1 - minRange1)
        mapped_value = minRange2 + (normalized_x * (maxRange2 - minRange2))
        return mapped_value

utils = Utils()  # util is global object
