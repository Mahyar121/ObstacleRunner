from game import *
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, game):

        self.JUMP_SOUND = pygame.mixer.Sound('red.wav')
        self.PUNCH_SOUND = pygame.mixer.Sound('blue.wav')
        self.KICK_SOUND = pygame.mixer.Sound('green.wav')

        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.spritesheet = Spritesheet(playerspritesheetFile)
        self.standing_frames = []
        self.punching_frames_l = []
        self.punching_frames_r = []
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.kicking_frames_l = []
        self.kicking_frames_r = []
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.rect = self.image.get_rect()
        self.rect.center = vector2(100, 530)
        self.position = vector2(100, 530)
        self.velocity = vector2(0, 0)
        self.acceleration = vector2(0, 0)
        self.jumping = False
        self.punching = False
        self.left = False
        self.right = True
        self.kicking = False
        self.tutorial = False
        self.tutorialLEFT = False
        self.tutorialRIGHT = False
        self.tutorialJUMP = False
        self.tutorialPUNCH = False
        self.tutorialKICK = False

    def jump(self):
        #jump if on platform
        self.rect.y += 2
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 2
        if hits and not self.jumping:
            self.jumping = True
            self.JUMP_SOUND.play()  # Added sound here- Michael
            self.velocity.y = -playerJump

    def jumpfall(self):
        if self.jumping:
            if self.velocity.y < -2:
                self.velocity.y = -2

    def load_images(self):
        # puts all the kicking frames in a list
        self.kicking_frames_r = [
            #self.spritesheet.get_image(32, 48, 16, 16),
            self.spritesheet.get_image(48, 48, 16, 16),
            self.spritesheet.get_image(64, 48, 16, 16)
        ]
        for kicking in self.kicking_frames_r:
            kicking.set_colorkey(graypink)
            self.kicking_frames_l.append(pygame.transform.flip(kicking, True, False))

        # puts all the punching frames in a list
        self.punching_frames_r = [
            self.spritesheet.get_image(16, 80, 16, 16),
            self.spritesheet.get_image(32, 80, 16, 16),
            self.spritesheet.get_image(48, 80, 16, 16)
        ]
        for punching in self.punching_frames_r:
            punching.set_colorkey(graypink)
        for frame in self.punching_frames_r:
            self.punching_frames_l.append(pygame.transform.flip(frame, True, False))
        # puts all the standing frames in a list
        self.standing_frames = [
            self.spritesheet.get_image(16, 16, 16, 16),
            self.spritesheet.get_image(32, 16, 16, 16),
            self.spritesheet.get_image(48, 16, 16, 16),
            self.spritesheet.get_image(64, 16, 16, 16)]
        for stand in self.standing_frames:
            stand.set_colorkey(graypink)
        # puts all the walking frames in a list
        walking = [self.spritesheet.get_image(16, 32, 16, 16),
                    self.spritesheet.get_image(32, 32, 16, 16),
                    self.spritesheet.get_image(48, 32, 16, 16),
                    self.spritesheet.get_image(64, 32, 16, 16),
                    self.spritesheet.get_image(80, 32, 16, 16),
                    self.spritesheet.get_image(96, 32, 16, 16),
                    ]
        # create walking frames facing right
        for frame in walking:
            self.walking_frames_r.append(frame)
        # create walking frames facing left
        for frame in self.walking_frames_r:
            self.walking_frames_l.append(pygame.transform.flip(frame, True, False))
        #player starts with the first walking frame that faces right
        self.image = self.walking_frames_r[0]
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.image.set_colorkey(graypink)
        # setting a reference for the rect
        self.rect = self.image.get_rect()

# SPRITE FUNCTION OVERRIDE
    def update(self):

        self.acceleration = vector2(0, playerGravity)
        key = pygame.key.get_pressed()
        if not self.tutorial:
            if key[pygame.K_LEFT] or key[pygame.K_a]:
                self.punching = False
                self.left = True
                self.right = False
                self.kicking = False
                self.walkingLeftanimation()
                self.acceleration.x = -playerAcceleration
            if key[pygame.K_RIGHT] or key[pygame.K_d]:
                self.punching = False
                self.right = True
                self.left = False
                self.kicking = False
                self.walkingRightanimation()
                self.acceleration.x = playerAcceleration
            if key[pygame.K_SPACE]:
                self.jump()
            if key[pygame.K_f]:
                self.punching = True
                self.PUNCH_SOUND.play()  # Added sound here - Michael
                if self.left:
                    self.punchingLeftAnimation()
                if self.right:
                    self.punchingRightAnimation()
            if key[pygame.K_g]:
                self.punching = False
                self.kicking = True
                self.KICK_SOUND.play()  # Added Sound here- Michael
                if self.left:
                    self.kickingLeftAnimation()
                if self.right:
                    self.kickingRightAnimation()
        elif self.tutorial:
            if key[pygame.K_LEFT] or key[pygame.K_a]:
                self.tutorialLEFT = True
                self.punching = False
                self.left = True
                self.right = False
                self.kicking = False
                self.walkingLeftanimation()
                self.acceleration.x = -playerAcceleration
            if key[pygame.K_RIGHT] or key[pygame.K_d] and self.tutorialLEFT:
                self.tutorialRIGHT = True
                self.punching = False
                self.right = True
                self.left = False
                self.kicking = False
                self.walkingRightanimation()
                self.acceleration.x = playerAcceleration
            if key[pygame.K_SPACE] and self.tutorialLEFT and self.tutorialRIGHT:
                self.tutorialJUMP = True
                self.jump()
            if key[pygame.K_f] and self.tutorialLEFT and self.tutorialRIGHT and self.tutorialJUMP:
                self.tutorialPUNCH = True
                self.punching = True
                if self.left:
                    self.punchingLeftAnimation()
                if self.right:
                    self.punchingRightAnimation()
            if key[pygame.K_g] and self.tutorialLEFT and self.tutorialRIGHT and self.tutorialJUMP \
                    and self.tutorialPUNCH:
                self.tutorialKICK = True
                self.punching = False
                self.kicking = True
                if self.left:
                    self.kickingLeftAnimation()
                if self.right:
                    self.kickingRightAnimation()
            if key[pygame.K_q]:
                from MainMenu import MainMenu
                MainMenu().game_intro()
        # calls the standing animation
        if self.velocity.x <= 0 and not self.punching and not self.jumping and not self.kicking:
            self.standingAnimation()

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
            self.image = pygame.transform.scale(self.image, (90, 90))
            self.image.set_colorkey(graypink)
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
        self.mask = pygame.mask.from_surface(self.image)

    def walkingRightanimation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 180:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.walking_frames_r)
            bottom = self.rect.bottom
            self.image = self.walking_frames_r[self.current_frame]
            self.image = pygame.transform.scale(self.image, (90, 90))
            self.image.set_colorkey(graypink)
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
        self.mask = pygame.mask.from_surface(self.image)

    def standingAnimation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 350:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
            bottom = self.rect.bottom
            self.image = self.standing_frames[self.current_frame]
            self.image = pygame.transform.scale(self.image, (90, 90))
            self.image.set_colorkey(graypink)
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
        self.mask = pygame.mask.from_surface(self.image)

    def punchingRightAnimation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 200:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.punching_frames_r)
            bottom = self.rect.bottom
            self.image = self.punching_frames_r[self.current_frame]
            self.image = pygame.transform.scale(self.image, (90, 90))
            self.image.set_colorkey(graypink)
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
        self.mask = pygame.mask.from_surface(self.image)

    def punchingLeftAnimation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 200:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.punching_frames_l)
            bottom = self.rect.bottom
            self.image = self.punching_frames_l[self.current_frame]
            self.image = pygame.transform.scale(self.image, (90, 90))
            self.image.set_colorkey(graypink)
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
        self.mask = pygame.mask.from_surface(self.image)

    def kickingRightAnimation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 200:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.kicking_frames_r)
            bottom = self.rect.bottom
            self.image = self.kicking_frames_r[self.current_frame]
            self.image = pygame.transform.scale(self.image, (90, 90))
            self.image.set_colorkey(graypink)
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
        self.mask = pygame.mask.from_surface(self.image)

    def kickingLeftAnimation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 200:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.kicking_frames_l)
            bottom = self.rect.bottom
            self.image = self.kicking_frames_l[self.current_frame]
            self.image = pygame.transform.scale(self.image, (90, 90))
            self.image.set_colorkey(graypink)
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
        self.mask = pygame.mask.from_surface(self.image)


