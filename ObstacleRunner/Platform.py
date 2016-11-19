from Settings import *
import pygame

# level 1 platform
PLATFORM_LIST = [(0, display_height - 40, display_width, 40),
                 (display_width / 2 - 50, display_height * 3 / 4, 100, 20),
                 (125, display_height - 350, 100, 20),
                 (350, 200, 100, 20),
                 (175, 100, 50, 20)]


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width,height))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
