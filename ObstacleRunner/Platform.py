from Settings import *
import pygame
from random import *

PLATFORM_LIST = [
    (0, display_height- 70), (500, display_height - 70),(100, display_height - 280),(300, display_height - 490),
    (200, display_height - 700), (500, display_height - 910), (300, display_height - 1130),
    (100, display_height - 1340), (400, display_height - 1550)
]


class Platform(pygame.sprite.Sprite):
    def __init__(self, game, x , y,):
        self._layer = PLATFORM_LAYER
        self.groups = game.all_sprites, game.platforms
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = [self.game.platformSpriteSheet.get_image(0, 384, 380, 94)]
        self.image = choice(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if randrange(20) < COIN_SPAWN_RATE:
            from Coin import Coin
            Coin(self.game, self)



