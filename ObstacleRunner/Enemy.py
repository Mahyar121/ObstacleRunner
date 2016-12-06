from Settings import *
from random import choice, randrange
'''
Mahyar Haji Babaie
mahyarhajibabaie@csu.fullerton.edu

Michael Franzen
mfranzen15@gmail.com

This file loads all the enemies and the location of where the enemyfly will spawn.
It also handles the AI of the enemies under the update functions
'''

ENEMYFLY_LIST = [(20, 300), (500, -300), (300, -900), (20, -1500), (600, -2200), (100, -2800),
                 (20, -3400), (50, -4000), (300, -4800), (400, -5500), (240, -5800), (300, -6400),
                 (0, -7000), (400, -7800), (0, -8400)
                 ]

# creates an enemy fly
class EnemyFly(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = ENEMY_LAYER
        self.groups = game.all_sprites, game.enemyFly
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.imageflyup = self.game.enemiesSpriteSheet.get_image(566, 510, 122, 139)
        self.imageflyup = pygame.transform.scale(self.imageflyup, (70, 70))
        self.imageflydown = self.game.enemiesSpriteSheet.get_image(568, 1534, 122, 135)
        self.imageflydown = pygame.transform.scale(self.imageflydown, (70, 70))
        self.image = self.imageflyup
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.velocityX = randrange(1, ENEMYFLY_SPEED)
        self.rect.y = y
        self.velocityY = 0
        self.directionY = 0.5
        self.directionX = 1

    # handles the movement of the fly
    def update(self):

        self.velocityY += self.directionY
        # changing the direction so it looks smooth
        if self.velocityY > ENEMYFLY_SPEED or self.velocityY < -ENEMYFLY_SPEED:
            self.directionY *= -1
        # using center to store location since they are differnt pixel sizes
        center = self.rect.center
        if self.directionY < 0:
            self.image = self.imageflyup
        else:
            self.image = self.imageflydown
        # repositioning the sprite
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = center
        self.rect.y += self.velocityY
        # if the mobs x is greater than the edge flip
        if self.rect.right > display_width - 60:
            self.directionX = -1
        # if the mobs x is less than the edge flip
        if self.rect.right < 60:
            self.directionX = 1

        self.rect.x += self.velocityX * self.directionX
        # if he flies off screen then dies
        if self.rect.left > display_width + 20 or self.rect.right < -20:
            self.kill()

class SpikeEnemy(pygame.sprite.Sprite):
    def __init__(self, game, plat):
        self._layer = ENEMY_LAYER
        self.groups = game.all_sprites, game.spikeenemy
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.plat = plat
        self.walking_l = []
        self.walking_r = [
            self.game.enemiesSpriteSheet.get_image(814, 1417, 90, 155),
            self.game.enemiesSpriteSheet.get_image(704, 1256, 120, 159),
            self.game.enemiesSpriteSheet.get_image(812, 296, 90, 155)
        ]

        for frames in self.walking_r:
            frames = pygame.transform.scale(frames, (50, 70))
            self.walking_l.append(pygame.transform.flip(frames, True, False))

        self.image = self.walking_r[0]
        self.image = pygame.transform.scale(self.image, (50, 70))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = self.plat.rect.centerx
        self.velocityX = ENEMYSPIKE_SPEED
        self.direction = 1
        self.last_update = 0
        self.current_frame = 0

    def update(self):
        self.rect.bottom = self.plat.rect.top - 2

        # if the mobs x is greater than the edge flip
        if self.rect.x > self.plat.rect.right - 60:
            self.direction = -1
        # if the mobs x is less than the edge flip
        if self.rect.x < self.plat.rect.left + 20:
            self.direction = 1

        self.rect.x += self.velocityX * self.direction

        # if platform gone then kill the mob
        if not self.game.platforms.has(self.plat):
            self.kill()


class BrownMob(pygame.sprite.Sprite):
    def __init__(self, game, plat):
        self._layer = ENEMY_LAYER
        self.groups = game.all_sprites, game.brownmob
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.plat = plat
        self.walking_l = []
        self.walkimage1 = pygame.image.load("mob2-1.png").convert()
        self.walkimage1.set_colorkey(darkred)
        self.walkimage2 = pygame.image.load("mob2-2.png").convert()
        self.walkimage2.set_colorkey(darkred)
        self.walking_r = [
            self.walkimage1,
            self.walkimage2
        ]

        for frames in self.walking_r:
            frames = pygame.transform.scale(frames, (70, 70))
            self.walking_l.append(pygame.transform.flip(frames, True, False))

        self.image = self.walking_r[0]
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = self.plat.rect.centerx
        self.velocityX = ENEMYBROWN_SPEED
        self.direction = 1
        self.last_update = 0
        self.current_frame = 0

    def update(self):
        self.rect.bottom = self.plat.rect.top - 2

        # if the mobs x is greater than the edge flip
        if self.rect.x > self.plat.rect.right - 60:
            self.direction = -1
        # if the mobs x is less than the edge flip
        if self.rect.x < self.plat.rect.left + 20:
            self.direction = 1

        if self.direction == -1:
            self.walkingRightanimation()
        else:
            self.walkingLeftanimation()
        self.rect.x += self.velocityX * self.direction

        # if platform gone then kill the mob
        if not self.game.platforms.has(self.plat):
            self.kill()

    def walkingLeftanimation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 180:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.walking_l)
            self.image = self.walking_l[self.current_frame]
            self.image = pygame.transform.scale(self.image, (70, 70))
            self.image.set_colorkey(darkred)
        self.mask = pygame.mask.from_surface(self.image)

    def walkingRightanimation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 180:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.walking_r)
            self.image = self.walking_r[self.current_frame]
            self.image = pygame.transform.scale(self.image, (70, 70))
            self.image.set_colorkey(darkred)
        self.mask = pygame.mask.from_surface(self.image)


class SkullMob(pygame.sprite.Sprite):
    def __init__(self, game, plat):
        self._layer = ENEMY_LAYER
        self.groups = game.all_sprites, game.skullmob
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.plat = plat
        self.walking_l = []
        self.walkimage1 = pygame.image.load("mob3-1.png").convert()
        self.walkimage1.set_colorkey(darkred)
        self.walkimage2 = pygame.image.load("mob3-2.png").convert()
        self.walkimage2.set_colorkey(darkred)
        self.walking_r = [
            self.walkimage1,
            self.walkimage2
        ]

        for frames in self.walking_r:
            frames = pygame.transform.scale(frames, (70, 70))
            self.walking_l.append(pygame.transform.flip(frames, True, False))

        self.image = self.walking_r[0]
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = self.plat.rect.centerx
        self.velocityX = ENEMYSKULL_SPEED
        self.direction = 1
        self.last_update = 0
        self.current_frame = 0

    def update(self):
        self.rect.bottom = self.plat.rect.top - 2

        # if the mobs x is greater than the edge flip
        if self.rect.x > self.plat.rect.right - 60:
            self.direction = -1
        # if the mobs x is less than the edge flip
        if self.rect.x < self.plat.rect.left + 20:
            self.direction = 1

        if self.direction == -1:
            self.walkingRightanimation()
        else:
            self.walkingLeftanimation()
        self.rect.x += self.velocityX * self.direction

        # if platform gone then kill the mob
        if not self.game.platforms.has(self.plat):
            self.kill()

    def walkingLeftanimation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 180:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.walking_l)
            self.image = self.walking_l[self.current_frame]
            self.image = pygame.transform.scale(self.image, (70, 70))
            self.image.set_colorkey(darkred)
        self.mask = pygame.mask.from_surface(self.image)

    def walkingRightanimation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 180:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.walking_r)
            self.image = self.walking_r[self.current_frame]
            self.image = pygame.transform.scale(self.image, (70, 70))
            self.image.set_colorkey(darkred)
        self.mask = pygame.mask.from_surface(self.image)


class DigletMob(pygame.sprite.Sprite):
    def __init__(self, game, plat):
        self._layer = ENEMY_LAYER
        self.groups = game.all_sprites, game.digletmob
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.plat = plat
        self.walking_l = []
        self.walkimage1 = pygame.image.load("mob4-1.png").convert()
        self.walkimage1.set_colorkey(darkred)
        self.walkimage2 = pygame.image.load("mob4-2.png").convert()
        self.walkimage2.set_colorkey(darkred)
        self.walking_r = [
            self.walkimage1,
            self.walkimage2
        ]

        for frames in self.walking_r:
            frames = pygame.transform.scale(frames, (70, 70))
            self.walking_l.append(pygame.transform.flip(frames, True, False))

        self.image = self.walking_r[0]
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = self.plat.rect.centerx
        self.velocityX = ENEMYDIG_SPEED
        self.direction = 1
        self.last_update = 0
        self.current_frame = 0

    def update(self):
        self.rect.bottom = self.plat.rect.top - 2

        # if the mobs x is greater than the edge flip
        if self.rect.x > self.plat.rect.right - 60:
            self.direction = -1
        # if the mobs x is less than the edge flip
        if self.rect.x < self.plat.rect.left + 20:
            self.direction = 1

        if self.direction == -1:
            self.walkingRightanimation()
        else:
            self.walkingLeftanimation()
        self.rect.x += self.velocityX * self.direction

        # if platform gone then kill the mob
        if not self.game.platforms.has(self.plat):
            self.kill()

    def walkingLeftanimation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 180:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.walking_l)
            self.image = self.walking_l[self.current_frame]
            self.image = pygame.transform.scale(self.image, (50, 70))
            self.image.set_colorkey(darkred)
        self.mask = pygame.mask.from_surface(self.image)

    def walkingRightanimation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 180:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.walking_r)
            self.image = self.walking_r[self.current_frame]
            self.image = pygame.transform.scale(self.image, (50, 70))
            self.image.set_colorkey(darkred)
        self.mask = pygame.mask.from_surface(self.image)






