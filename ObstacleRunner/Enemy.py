from Settings import *
from random import choice, randrange


# creates an enemy fly
class EnemyFly(pygame.sprite.Sprite):
    def __init__(self, game):
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
        self.rect.centerx = 30
        self.velocityX = randrange(1, ENEMYFLY_SPEED)
        self.rect.y = randrange(display_height / 2)
        self.velocityY = 0
        self.directionY = 0.5

    # handles the movement of the fly
    def update(self):
        self.rect.x += self.velocityX
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






