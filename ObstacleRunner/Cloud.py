from Settings import *
from random import choice, randrange


# class that is in charge of putting clouds on the screen
class Cloud(pygame.sprite.Sprite):
    def __init__(self, game):
        self._layer = CLOUD_LAYER
        self.groups = game.all_sprites, game.clouds
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = choice(self.game.cloud_images)
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        scale = randrange(80, 110) / 100
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * scale), int(self.rect.height * scale)))
        self.rect.x = randrange(display_width - self.rect.width)
        self.rect.y = randrange(-500, -50)

    def update(self):
        if self.rect.top > display_height * 2:
            self.kill()


