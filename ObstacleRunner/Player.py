from Settings import *
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load("player.png").convert()
        # makes the image transparent by removing the black square around it
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = (display_width / 2, display_height / 2)
        self.position = vector2(display_width / 2, display_height / 2)
        self.velocity = vector2(0, 0)
        self.acceleration = vector2(0, 0)

    def jump(self):
        # jump if on a platform
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.velocity.y = -playerJump

# SPRITE FUNCTION OVERRIDE
    def update(self):
        self.acceleration = vector2(0, playerGravity)
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.acceleration.x = -playerAcceleration
        if key[pygame.K_RIGHT]:
            self.acceleration.x = playerAcceleration
        if key[pygame.K_SPACE]:
            self.jump()

        # equation for friction to slow player down on X direction
        self.acceleration.x += self.velocity.x * playerFriction
        # equation for motion
        self.velocity.x += self.acceleration.x
        self.velocity.y += self.acceleration.y
        self.position.x += self.velocity.x + 0.5 * self.acceleration.x
        self.position.y += self.velocity.y + 0.5 * self.acceleration.y
        # wraps around screen
        if self.position.x > display_width:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = display_width

        self.rect.midbottom = self.position


