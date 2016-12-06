from Settings import *
import pygame
from pygame.locals import *
'''
Mahyar Haji Babaie
mahyarhajibabaie@csu.fullerton.edu

Michael Franzen
mfranzen15@gmail.com

This file loads sprites from a spritesheet
'''


# will handle spritesheet
class Spritesheet(object):
    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        # creates a blank image
        image = pygame.Surface((width, height))
        # copy the sprite from the big sheet into a smaller image
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        # making image transparent
        image.set_colorkey(black)
        return image
