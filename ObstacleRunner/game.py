#!/usr/bin/python

import random
import os
import pygame
from MainMenu import *
from Player import *
from Platform import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(title)
        pygame.font.init()
        self.fileName = "HighScore.json"
        # if there is no file then make one
        if not os.path.isfile(self.fileName):
            empty_score_file = open(self.fileName, "w")
            empty_score_file.write("[]")
            empty_score_file.close()
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.player = Player(self)
        self.running = True


    def new(self):
        # start a new game, reset everything
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        # creates a platform
        for platform in PLATFORM_LIST:
            plat = Platform(*platform)
            self.all_sprites.add(plat)
            self.platforms.add(plat)

        self.gameLoop()

    def gameLoop(self):
        self.running = True
        while self.running:
            clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def update(self):
        self.all_sprites.update()

        if self.player.velocity.y > 0:
            player_collision = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if player_collision:
                # if the player comes in contact with platform, put him at the top of the platform hitbox
                self.player.position.y = player_collision[0].rect.top
                self.player.velocity.y = 0
        # if player reaches top of the screen move the camera
        if self.player.rect.top <= display_height / 4:
            self.player.position.y += abs(self.player.velocity.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.velocity.y)
                if plat.rect.top >= display_height:
                    plat.kill()

        # player death
        if self.player.rect.bottom > display_height:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.velocity.y, 7)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platforms) == 0:
            pygame.quit()

        # spawn new platforms
        while len(self.platforms) < 10:
            width = random.randrange(50, 100)
            p = Platform(random.randrange(0, display_width - width),
                         random.randrange(-75, -30),
                         width, 20)
            self.platforms.add(p)
            self.all_sprites.add(p)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



    def draw(self):
        screen.fill(black)
        self.all_sprites.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    Game()
    MainMenu().game_intro()
    quit()



