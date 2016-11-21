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
        self.groups = game.all_sprites, game.platforms
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = [self.game.platformSpriteSheet.get_image(0, 384, 380, 94)]
        self.image = choice(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if randrange(20) < COIN_SPAWN_RATE:
            Coin(self.game, self)


class Coin(pygame.sprite.Sprite):
    def __init__(self, game, plat):
        self.groups = game.all_sprites, game.coin
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.plat = plat
        self.type = choice(["coin"])
        self.image = pygame.image.load("coin.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.plat.rect.centerx
        self.rect.bottom = self.plat.rect.top - 5

    def update(self):
        self.rect.bottom = self.plat.rect.top - 5
        if not self.game.platforms.has(self.plat):
            self.kill()


