from Settings import *
import pygame
from random import *

# X and Y coordinates to spawn grass platforms
GRASS_BIG_PLATFORM_LIST = [(-70, 530), (500, 530), (100, 300), (100, -500), (100, -900)]
GRASS_SMALL_PLATFORM_LIST = [(20, 100), (300, 100), (600, 100), (200, -100), (500, -100), (350, -300), (500, -700)]
# X and Y coordinates to spawn brown cake platforms
BCAKE_BIG_PLATFORM_LIST = [(-70, -1100), (500, -1100), (500, -2100)]
BCAKE_SMALL_PLATFORM_LIST = [(20, -1300), (300, -1300), (600, -1300), (200, -1500), (500, -1700), (300, -1900),
                             (50, -2300), (300, -2500), (100, -2700), (500, -2700), (300, -2900)]
# X and Y coordinates to spawn sand platforms
SAND_BIG_PLATFORM_LIST = [(-70, -3100), (500, -3100), (250, -3900), (100, -4100)]
SAND_SMALL_PLATFORM_LIST = [(20, -3300), (600, -3300), (100, -3500), (500, -3500), (20, -3700), (500, -3700)]
# X and Y coordinates to spawn snow platforms
SNOW_BIG_PLATFORM_LIST = [(-70, -4300), (500, -4300), (300, -5700), (0, -5900)]
SNOW_SMALL_PLATFORM_LIST = [(100, -4500), (300, -4700), (0, -4900), (600, -5100), (0, -5300), (600, -5500),
                            (350, -6100)]

# make abstract class for platforms


class GrassBigPlatform(pygame.sprite.Sprite):
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
        randomvalue = randrange(100)
        if randomvalue < GOLD_COIN_SPAWN_RATE:
            from Coin import GoldCoin
            GoldCoin(self.game, self)
        elif randomvalue < SILVER_COIN_SPAWN_RATE:
            from Coin import SilverCoin
            SilverCoin(self.game, self)
        elif randomvalue < BRONZE_COIN_SPAWN_RATE:
            from Coin import BronzeCoin
            BronzeCoin(self.game, self)


class GrassSmallPlatform(pygame.sprite.Sprite):
    def __init__(self, game, x , y,):
        self._layer = PLATFORM_LAYER
        self.groups = game.all_sprites, game.platforms
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = [self.game.platformSpriteSheet.get_image(382, 204, 200, 100)]
        self.image = choice(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        randomvalue = randrange(100)
        if randomvalue < GOLD_COIN_SPAWN_RATE:
            from Coin import GoldCoin
            GoldCoin(self.game, self)
        elif randomvalue < SILVER_COIN_SPAWN_RATE:
            from Coin import SilverCoin
            SilverCoin(self.game, self)
        elif randomvalue < BRONZE_COIN_SPAWN_RATE:
            from Coin import BronzeCoin
            BronzeCoin(self.game, self)


class BCakeBigPlatform(pygame.sprite.Sprite):
    def __init__(self, game, x , y,):
        self._layer = PLATFORM_LAYER
        self.groups = game.all_sprites, game.platforms
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = [self.game.platformSpriteSheet.get_image(0, 0, 380, 94)]
        self.image = choice(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        randomvalue = randrange(100)
        if randomvalue < GOLD_COIN_SPAWN_RATE:
            from Coin import GoldCoin
            GoldCoin(self.game, self)
        elif randomvalue < SILVER_COIN_SPAWN_RATE:
            from Coin import SilverCoin
            SilverCoin(self.game, self)
        elif randomvalue < BRONZE_COIN_SPAWN_RATE:
            from Coin import BronzeCoin
            BronzeCoin(self.game, self)

class BCakeSmallPlatform(pygame.sprite.Sprite):
    def __init__(self, game, x , y,):
        self._layer = PLATFORM_LAYER
        self.groups = game.all_sprites, game.platforms
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = [self.game.platformSpriteSheet.get_image(262, 1152, 200, 100)]
        self.image = choice(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        randomvalue = randrange(100)
        if randomvalue < GOLD_COIN_SPAWN_RATE:
            from Coin import GoldCoin
            GoldCoin(self.game, self)
        elif randomvalue < SILVER_COIN_SPAWN_RATE:
            from Coin import SilverCoin
            SilverCoin(self.game, self)
        elif randomvalue < BRONZE_COIN_SPAWN_RATE:
            from Coin import BronzeCoin
            BronzeCoin(self.game, self)


class SandBigPlatform(pygame.sprite.Sprite):
    def __init__(self, game, x , y,):
        self._layer = PLATFORM_LAYER
        self.groups = game.all_sprites, game.platforms
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = [self.game.platformSpriteSheet.get_image(0, 1056, 380, 94)]
        self.image = choice(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        randomvalue = randrange(100)
        if randomvalue < GOLD_COIN_SPAWN_RATE:
            from Coin import GoldCoin
            GoldCoin(self.game, self)
        elif randomvalue < SILVER_COIN_SPAWN_RATE:
            from Coin import SilverCoin
            SilverCoin(self.game, self)
        elif randomvalue < BRONZE_COIN_SPAWN_RATE:
            from Coin import BronzeCoin
            BronzeCoin(self.game, self)


class SandSmallPlatform(pygame.sprite.Sprite):
    def __init__(self, game, x , y,):
        self._layer = PLATFORM_LAYER
        self.groups = game.all_sprites, game.platforms
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = [self.game.platformSpriteSheet.get_image(382, 102, 200, 100)]
        self.image = choice(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        randomvalue = randrange(100)
        if randomvalue < GOLD_COIN_SPAWN_RATE:
            from Coin import GoldCoin
            GoldCoin(self.game, self)
        elif randomvalue < SILVER_COIN_SPAWN_RATE:
            from Coin import SilverCoin
            SilverCoin(self.game, self)
        elif randomvalue < BRONZE_COIN_SPAWN_RATE:
            from Coin import BronzeCoin
            BronzeCoin(self.game, self)


class SnowBigPlatform(pygame.sprite.Sprite):
    def __init__(self, game, x , y,):
        self._layer = PLATFORM_LAYER
        self.groups = game.all_sprites, game.platforms
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = [self.game.platformSpriteSheet.get_image(0, 480, 380, 94)]
        self.image = choice(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        randomvalue = randrange(100)
        if randomvalue < GOLD_COIN_SPAWN_RATE:
            from Coin import GoldCoin
            GoldCoin(self.game, self)
        elif randomvalue < SILVER_COIN_SPAWN_RATE:
            from Coin import SilverCoin
            SilverCoin(self.game, self)
        elif randomvalue < BRONZE_COIN_SPAWN_RATE:
            from Coin import BronzeCoin
            BronzeCoin(self.game, self)

class SnowSmallPlatform(pygame.sprite.Sprite):
    def __init__(self, game, x , y,):
        self._layer = PLATFORM_LAYER
        self.groups = game.all_sprites, game.platforms
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = [self.game.platformSpriteSheet.get_image(382, 306, 200, 100)]
        self.image = choice(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        randomvalue = randrange(100)
        if randomvalue < GOLD_COIN_SPAWN_RATE:
            from Coin import GoldCoin
            GoldCoin(self.game, self)
        elif randomvalue < SILVER_COIN_SPAWN_RATE:
            from Coin import SilverCoin
            SilverCoin(self.game, self)
        elif randomvalue < BRONZE_COIN_SPAWN_RATE:
            from Coin import BronzeCoin
            BronzeCoin(self.game, self)

