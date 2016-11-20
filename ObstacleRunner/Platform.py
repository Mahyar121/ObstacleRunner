from Settings import *
import pygame
from random import choice

PLATFORM_LIST = [
    # row 1
    (0, display_height- 70), (70, display_height - 70),(140, display_height - 70),
    (730, display_height - 70), (660, display_height - 70), (590, display_height - 70),
    # row 2
    (30, display_height - 280), (100, display_height - 280), (170, display_height - 280),
    # row 3
    (60, display_height - 490), (130, display_height - 490), (200, display_height - 490),
    # row 4
    (100, display_height - 700), (170, display_height - 700), (210, display_height - 700),
    # row 5
    (150, display_height - 910), (220, display_height - 910), (290, display_height - 910),
    # row 6
    (300, display_height - 1130), (370, display_height - 1130), (440, display_height - 1130),



]




class Platform(pygame.sprite.Sprite):
    def __init__(self, game, x , y,):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = [self.game.platformSpriteSheet.get_image(504, 576, 70, 70)]
        self.image = choice(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
