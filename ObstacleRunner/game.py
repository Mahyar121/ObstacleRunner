#!/usr/bin/python

import os
from MainMenu import *
from Platform import *
from HighScores import *
from Spritesheet import *
import random

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(title)
        pygame.font.init()
        self.font = pygame.font.Font(FONTNAME, 20)
        self.fileName = "HighScore.json"
        # if there is no file then make one
        if not os.path.isfile(self.fileName):
            empty_score_file = open(self.fileName, "w")
            empty_score_file.write("[]")
            empty_score_file.close()
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        from Player import Player
        self.player = Player(self)
        self.running = True
        self.playerDead = False
        self.highscore = HighScores()
        self.platformSpriteSheet = Spritesheet(spritesheetPlatformFile)
        self.coin = pygame.sprite.Group()


    def new(self):
        # start a new game, reset everything
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        from Player import Player
        self.player = Player(self)
        self.highscore = HighScores()
        self.playerDead = False
        self.coin = pygame.sprite.Group()
        self.platformSpriteSheet = Spritesheet(spritesheetPlatformFile)
        # creates a platform
        for platform in PLATFORM_LIST:
            Platform(self, *platform)
        self.gameLoop()

    def gameLoop(self):
        self.running = True
        while self.running:
            clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            pygame.display.update()
        pygame.quit()

    def update(self):
        self.all_sprites.update()
        if self.player.velocity.y > 0:
            player_collision = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if player_collision:
                lowest = player_collision[0]
                for hit in player_collision:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                # make sure the player falls off if leaves past the right or left of platform
                if self.player.position.x < lowest.rect.right + 10:
                    if self.player.position.x > lowest.rect.left - 10:
                        if self.player.position.y < lowest.rect.centery:
                            self.player.position.y = lowest.rect.top
                            self.player.velocity.y = 0
                            self.player.jumping = False
        # if player reaches top of the screen move the camera
        if self.player.rect.top <= display_height / 4:
            self.player.position.y += max(abs(self.player.velocity.y), 2)
            # move platforms down based on player speed
            for plat in self.platforms:
                plat.rect.y += max(abs(self.player.velocity.y), 2)
                if plat.rect.top >= display_height:
                    plat.kill()
                    self.highscore.score += 10
        # if player hits coin
        coin_hits = pygame.sprite.spritecollide(self.player, self.coin, True)
        for chits in coin_hits:
            if chits.type == "coin":
                self.highscore.score += 100
                chits.kill()

        # player death
        if self.player.rect.bottom > display_height:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.velocity.y, 7)
                if sprite.rect.bottom < 0:
                    sprite.kill()
                    self.playerDead = True

        '''
        # spawn new platforms
        while len(self.platforms) < 5:
            width = random.randrange(0, 500)
            Platform(self, random.randrange(0, display_width - width),
                         random.randrange(10, 30))

        '''
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.player.jumpfall()

    def draw(self):
        screen.fill(teal)
        self.all_sprites.draw(screen)
        screen.blit(self.player.image, self.player.rect)
        screen.blit(self.font.render("Score: {}".format(self.highscore.score), -1, white), (500, 10))
        if self.playerDead:
            highscore = 1
            screen.blit(pygame.font.Font(FONTNAME, 100).render("Game Over", -1, red), (100, 70))
            if highscore == 1:
                screen.blit(
                    pygame.font.Font(FONTNAME, 30).render("Enter your name for the HighScore List", -1,
                                                          white), (10, 450))
                self.highscore.getUserName(self.highscore.score)
                self.highscore.addHighScores(self.highscore.score)
                highscore = 0
                from MainMenu import MainMenu
                MainMenu().game_intro()
        pygame.display.flip()


if __name__ == "__main__":
    Game()
    MainMenu().game_intro()
    quit()



