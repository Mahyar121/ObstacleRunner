from Settings import *
from random import choice, randrange


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
        self.rect.centerx = choice([-100, display_width + 100])
        self.velocityX = randrange(1,4)
        if self.rect.centerx > display_width:
            self.velocityX *= -1
        self.rect.y = randrange(display_height / 2)
        self.velocityY = 0
        self.directionY = 0.5

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
        if self.rect.left > display_width + 100 or self.rect.right < -100:
            self.kill()