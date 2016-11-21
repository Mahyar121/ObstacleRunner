from game import *
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.spritesheet = Spritesheet(playerspritesheetFile)
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.rect = self.image.get_rect()
        self.rect.center = vector2(100, 530)
        self.position = vector2(100, 530)
        self.velocity = vector2(0, 0)
        self.acceleration = vector2(0, 0)
        self.jumping = False



    def jump(self):
        #jump if on platform
        self.rect.y += 2
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 2
        if hits and not self.jumping:
            self.jumping = True
            self.velocity.y = -playerJump

    def jumpfall(self):
        if self.jumping:
            if self.velocity.y < -2:
                self.velocity.y = -2

    def load_images(self):

        # putting all walking images into a list
        walkingimages = [self.spritesheet.get_image(0, 0, 66, 90),
                         self.spritesheet.get_image(66, 0, 66, 90),
                         self.spritesheet.get_image(132, 0, 67, 90),
                         self.spritesheet.get_image(0, 93, 66, 90),
                         self.spritesheet.get_image(66, 93, 66, 90),
                         self.spritesheet.get_image(132, 93, 72, 90),
                         self.spritesheet.get_image(0, 186, 70, 90)
                        ]
        # create walking frames facing right
        for frame in walkingimages:
            self.walking_frames_r.append(frame)
        # create walking frames facing left
        for frame in self.walking_frames_r:
            self.walking_frames_l.append(pygame.transform.flip(frame, True, False))

        #player starts with the first walking frame that faces right
        self.image = self.walking_frames_r[0]

        # setting a reference for the rect
        self.rect = self.image.get_rect()



# SPRITE FUNCTION OVERRIDE
    def update(self):
        self.acceleration = vector2(0, playerGravity)
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.walkingLeftanimation()
            self.acceleration.x = -playerAcceleration
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.walkingRightanimation()
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

    def walkingLeftanimation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 180:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.walking_frames_l)
            bottom = self.rect.bottom
            self.image = self.walking_frames_l[self.current_frame]
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom

    def walkingRightanimation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 180:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.walking_frames_r)
            bottom = self.rect.bottom
            self.image = self.walking_frames_r[self.current_frame]
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom



