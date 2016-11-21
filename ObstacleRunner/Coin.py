from Settings import *
from random import choice


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

