import pygame.draw

from utils import utils


class Circle:
    def __init__(self, pos, radius):
        self.pos = pos
        self.radius = radius

    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(utils.screen, (233, 233, 233), self.pos, self.radius, 2)
