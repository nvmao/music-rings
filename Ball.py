import random
import pygame
from pygame import Vector2

from utils import utils


class Ball:
    def __init__(self, pos, radius=10, color=(255, 255, 255)):
        self.color = color
        self.radius = radius
        self.pos = pos

    def draw(self):
        pygame.draw.circle(utils.screen, self.color, self.pos, self.radius)
