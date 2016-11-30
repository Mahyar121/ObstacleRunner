from Settings import *
from random import choice


# displays gold coins on the screen
class GoldCoin(pygame.sprite.Sprite):
    def __init__(self, game, plat):
        self._layer = COIN_LAYER
        self.groups = game.all_sprites, game.coin
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.plat = plat
        self.type = choice(["goldcoin"])
        self.image = self.game.coinSpriteSheet.get_image(244, 1981, 61, 61)
        self.image.set_colorkey(black)
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.plat.rect.centerx
        self.rect.bottom = self.plat.rect.top - 1

    # updates the gold coin
    def update(self):
        if not self.game.platforms.has(self.plat):
            self.kill()


# displays the silver coins on the screen
class SilverCoin(pygame.sprite.Sprite):
    def __init__(self, game, plat):
        self._layer = COIN_LAYER
        self.groups = game.all_sprites, game.coin
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.plat = plat
        self.type = choice(["silvercoin"])
        self.image = self.game.coinSpriteSheet.get_image(307, 1981, 61, 61)
        self.image.set_colorkey(black)
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.plat.rect.centerx
        self.rect.bottom = self.plat.rect.top - 1
    # updates the silver coin
    def update(self):
        self.rect.bottom = self.plat.rect.top - 1
        if not self.game.platforms.has(self.plat):
            self.kill()


# displays the bronze coins on the screen
class BronzeCoin(pygame.sprite.Sprite):
    def __init__(self, game, plat):
        self._layer = COIN_LAYER
        self.groups = game.all_sprites, game.coin
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.plat = plat
        self.type = choice(["bronzecoin"])
        self.image = self.game.coinSpriteSheet.get_image(329, 1390, 60, 61)
        self.image.set_colorkey(black)
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.plat.rect.centerx
        self.rect.bottom = self.plat.rect.top - 1
    # updates the bronze coin
    def update(self):
        self.rect.bottom = self.plat.rect.top - 1
        if not self.game.platforms.has(self.plat):
            self.kill()


class GoalBalloon(pygame.sprite.Sprite):
    def __init__(self, game, plat):
        self._layer = COIN_LAYER
        self.groups = game.all_sprites, game.coin
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.plat = plat
        self.type = choice(["goalcoin"])
        self.image = pygame.image.load("balloon.png")
        self.image.set_colorkey(black)
        self.image = pygame.transform.scale(self.image, (380, 200))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.plat.rect.centerx
        self.rect.bottom = self.plat.rect.top - 5

    def update(self):
        self.rect.bottom = self.plat.rect.top - 5