#!/usr/bin/python

import os
from MainMenu import *
from Platform import *
from HighScores import *
from Spritesheet import *
from Enemy import *

# class were the game will be loaded from
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
        self.running = True
        self.playerDead = False
        self.win = False
        self.highscore = HighScores()
        self.platformSpriteSheet = Spritesheet(spritesheetPlatformFile)
        self.enemiesSpriteSheet = Spritesheet(enemyspritesheetFile)
        self.coinSpriteSheet = Spritesheet(spritesheetPlatformFile)
        self.cloud_images = []
        for cloud in range(1, 4):
            self.cloud_images.append(pygame.image.load("cloud{}.png".format(cloud)).convert())

# used to refresh the games settings for when the player plays again
    def new(self):
        # start a new game, reset everything
        self.win = False
        self.loadSprites()
        self.gameLoop()
    # runs the game
    def gameLoop(self):
        self.running = True
        while self.running:
            clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            pygame.display.update()
        pygame.quit()

    # updates the game actions
    def update(self):
        self.all_sprites.update()
        self.enemy_collisions()
        self.coin_collisions()
        self.moving_camera()
        self.player_death()

    def events(self):
        # if player clicks on X quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # after the play presses the jump button, they will fall down at a realistic speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.player.jumpfall()

    # displays the images on the screen
    def draw(self):
        screen.fill(teal)
        self.all_sprites.draw(screen)
        scoreFont = pygame.font.Font(FONTNAME, 30)
        screen.blit(scoreFont.render("Score: {}".format(self.highscore.score), -1, black), (501, 11))
        screen.blit(scoreFont.render("Score: {}".format(self.highscore.score), -1, white), (500, 10))
        if self.win:
            highscore = 1
            screen.blit(pygame.font.Font(FONTNAME, 100).render("YOU WON!", -1, white), (102, 72))
            screen.blit(pygame.font.Font(FONTNAME, 100).render("YOU WON!", -1, red), (100, 70))
            if highscore == 1:
                screen.blit(
                    pygame.font.Font(FONTNAME, 33).render("Enter your name for the HighScore List", -1,
                                                          black), (10, 450))
                screen.blit(
                    pygame.font.Font(FONTNAME, 33).render("Enter your name for the HighScore List", -1,
                                                          white), (11, 452))
                self.highscore.getUserName(self.highscore.score)
                self.highscore.addHighScores(self.highscore.score)
                highscore = 0
                from MainMenu import MainMenu
                MainMenu().game_intro()
        if self.playerDead:
            highscore = 1
            screen.blit(pygame.font.Font(FONTNAME, 100).render("Game Over", -1, white), (102, 72))
            screen.blit(pygame.font.Font(FONTNAME, 100).render("Game Over", -1, red), (100, 70))
            if highscore == 1:
                screen.blit(
                    pygame.font.Font(FONTNAME, 33).render("Enter your name for the HighScore List", -1,
                                                          black), (10, 450))
                screen.blit(
                    pygame.font.Font(FONTNAME, 33).render("Enter your name for the HighScore List", -1,
                                                          white), (11, 452))
                self.highscore.getUserName(self.highscore.score)
                self.highscore.addHighScores(self.highscore.score)
                highscore = 0
                from MainMenu import MainMenu
                MainMenu().game_intro()
        pygame.display.flip()

    def tutorialPage(self):
        seconds = 5
        mainmenuSeconds = 0
        key = pygame.key.get_pressed()
        clock = pygame.time.Clock()
        tutorialCount = 0
        tutorialFPScount = 0
        tutorialExit = False
        bigFont = pygame.font.Font(FONTNAME, 40)
        medFont = pygame.font.Font(FONTNAME, 30)
        self.loadSprites()

        while not tutorialExit:
            self.player.tutorial = True
            clock.tick(FPS)
            screen.fill(teal)
            self.all_sprites.update()
            self.enemy_collisions()
            self.coin_collisions()
            self.player_death()
            self.all_sprites.draw(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            screen.blit(medFont.render("Type Q to exit tutorial", -1, white), (60, 8))
            screen.blit(medFont.render("Type Q to exit tutorial", -1, red), (62, 6))

            if not self.player.tutorialLEFT:
                screen.blit(medFont.render("Press A or Left Arrow to move left", -1, brightGreen), (12, 42))
                screen.blit(medFont.render("Press A or Left Arrow to move left", -1, black), (10, 40))
            if self.player.tutorialLEFT and not self.player.tutorialRIGHT and not self.player.tutorialJUMP \
                    and not self.player.tutorialPUNCH and not self.player.tutorialKICK:
                screen.blit(medFont.render("Press D or Right Arrow to move right", -1, brightGreen), (12, 42))
                screen.blit(medFont.render("Press D or Right Arrow to move right", -1, black), (10, 40))

            if self.player.tutorialLEFT and self.player.tutorialRIGHT and not self.player.tutorialJUMP \
                    and not self.player.tutorialPUNCH and not self.player.tutorialKICK:
                screen.blit(medFont.render("Press SpaceBar to jump", -1, brightGreen), (12, 42))
                screen.blit(medFont.render("Press SpaceBar to jump", -1, black), (10, 40))
            if self.player.tutorialLEFT and self.player.tutorialRIGHT and self.player.tutorialJUMP \
                    and not self.player.tutorialPUNCH and not self.player.tutorialKICK:
                screen.blit(medFont.render("Press F to punch", -1, brightGreen), (12, 42))
                screen.blit(medFont.render("Press F to punch", -1, black), (10, 40))
            if self.player.tutorialLEFT and self.player.tutorialRIGHT and self.player.tutorialJUMP \
                    and self.player.tutorialPUNCH and not self.player.tutorialKICK:
                screen.blit(medFont.render("Press G to kick", -1, brightGreen), (12, 42))
                screen.blit(medFont.render("Press G to kick", -1, black), (10, 40))

            if self.player.tutorialLEFT and self.player.tutorialRIGHT and self.player.tutorialJUMP \
                    and self.player.tutorialPUNCH and self.player.tutorialKICK and tutorialCount == 0:
                screen.blit(medFont.render("Avoid the Flies!", -1, brightGreen), (12, 42))
                screen.blit(medFont.render("Avoid the Flies!", -1, black), (10, 40))
                screen.blit(medFont.render("If you touch them you die!", -1, brightGreen), (12, 82))
                screen.blit(medFont.render("If you touch them you die!", -1, black), (10, 80))
                tutorialFPScount += 1
                if tutorialFPScount == 700:
                    tutorialCount += 1
            if tutorialCount == 1:
                screen.blit(medFont.render("You gain points from killing mobs,", -1, brightGreen), (12, 42))
                screen.blit(medFont.render("You gain points from killing mobs,", -1, black), (10, 40))
                screen.blit(medFont.render("traveling, and collecting coins", -1, brightGreen), (12, 82))
                screen.blit(medFont.render("traveling, and collecting coins", -1, black), (10, 80))
                tutorialFPScount += 1
                if tutorialFPScount == 1100:
                    tutorialCount += 1
            if tutorialCount == 2:
                screen.blit(medFont.render("You will lose if get killed or fall", -1, brightGreen), (12, 42))
                screen.blit(medFont.render("You will lose if get killed or fall", -1, black),(10, 40))
                screen.blit(medFont.render("You will win if you reach the top", -1, brightGreen), (12, 82))
                screen.blit(medFont.render("You will win if you reach the top", -1, black), (10, 80))
                tutorialFPScount += 1
                if tutorialFPScount == 1500:
                    tutorialCount += 1
            if tutorialCount == 3:
                screen.blit(medFont.render("You can run across the screen and", -1, brightGreen), (12, 42))
                screen.blit(medFont.render("You can run across the screen and", -1, black), (10, 40))
                screen.blit(medFont.render("You will appear on the other side", -1, brightGreen), (12, 82))
                screen.blit(medFont.render("You will appear on the other side", -1, black), (10, 80))
                tutorialFPScount += 1
                if tutorialFPScount == 1900:
                    tutorialCount += 1
            if tutorialCount == 4:
                screen.blit(bigFont.render("You have completed the Tutorial!", -1, brightGreen), (12, 42))
                screen.blit(bigFont.render("You have completed the Tutorial!", -1, black), (10, 40))
                screen.blit(bigFont.render("Returning to MainMenu in {}".format(seconds), -1, brightGreen), (42, 82))
                screen.blit(bigFont.render("Returning to MainMenu in {}".format(seconds), -1, black), (40, 80))
                mainmenuSeconds += 1
                if mainmenuSeconds == 70:
                    mainmenuSeconds = 0
                    seconds -= 1
                if seconds == 0:
                    from MainMenu import MainMenu
                    MainMenu().game_intro()

            screen.blit(medFont.render("Score: {}".format(self.highscore.score), -1, black), (500, 8))
            screen.blit(medFont.render("Score: {}".format(self.highscore.score), -1, white), (501, 6))
            pygame.display.update()

    def loadSprites(self):
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.platforms = pygame.sprite.Group()
        self.coin = pygame.sprite.Group()
        self.enemyFly = pygame.sprite.Group()
        self.clouds = pygame.sprite.Group()
        self.spikeenemy = pygame.sprite.Group()
        self.brownmob = pygame.sprite.Group()
        self.skullmob = pygame.sprite.Group()
        self.digletmob = pygame.sprite.Group()
        self.EnemyFlyTimer = 0
        from Player import Player
        self.player = Player(self)
        self.highscore = HighScores()
        self.playerDead = False
        # creates the enemy flys
        for fly in ENEMYFLY_LIST:
            EnemyFly(self, *fly)
        # creates the big grass platform
        for grassbigplatform in GRASS_BIG_PLATFORM_LIST:
            GrassBigPlatform(self, *grassbigplatform)
        # creates the small grass platform
        for grasssmallplatform in GRASS_SMALL_PLATFORM_LIST:
            GrassSmallPlatform(self, *grasssmallplatform)
        # creates the big brown cake platform
        for bcakebigplatform in BCAKE_BIG_PLATFORM_LIST:
            BCakeBigPlatform(self, *bcakebigplatform)
        # creates the small brown cake platform
        for bcakesmallplatform in BCAKE_SMALL_PLATFORM_LIST:
            BCakeSmallPlatform(self, *bcakesmallplatform)
        # creates the big sand platform
        for sandbigplatform in SAND_BIG_PLATFORM_LIST:
            SandBigPlatform(self, *sandbigplatform)
        # creates the small sand platform
        for sandsmallplatform in SAND_SMALL_PLATFORM_LIST:
            SandSmallPlatform(self, *sandsmallplatform)
        # creates the big snow platform
        for snowbigplatform in SNOW_BIG_PLATFORM_LIST:
            SnowBigPlatform(self, *snowbigplatform)
        # creates the small snow platform
        for snowsmallplatform in SNOW_SMALL_PLATFORM_LIST:
            SnowSmallPlatform(self, *snowsmallplatform)
        # creates the big stone platform
        for stonebigplatform in STONE_BIG_PLATFORM_LIST:
            StoneBigPlatform(self, *stonebigplatform)
        # creates the small stone platform
        for stonesmallplatform in STONE_SMALL_PLATFORM_LIST:
            StoneSmallPlatform(self, *stonesmallplatform)
        # creates clouds on the map
        for i in range(8):
            from Cloud import Cloud
            cloud = Cloud(self)
            cloud.rect.y += 500

    def enemy_collisions(self):
        # template for killing enemies
        # enemyspike
        enemyspike_hits = pygame.sprite.spritecollide(self.player, self.spikeenemy, False, pygame.sprite.collide_mask)
        for spike in self.spikeenemy:
            if self.player.punching or self.player.kicking:
                if self.player.right:
                    if enemyspike_hits and spike.rect.x >= self.player.rect.x and spike.rect.y >= self.player.rect.y:
                        spike.kill()
                        self.highscore.score += 100
                if self.player.left:
                    if enemyspike_hits and spike.rect.x <= self.player.rect.x and spike.rect.y >= self.player.rect.y:
                        spike.kill()
                        self.highscore.score += 100
            elif enemyspike_hits:
                self.playerDead = True

        # check if hits enemyfly
        enemyfly_hits = pygame.sprite.spritecollide(self.player, self.enemyFly, False, pygame.sprite.collide_mask)
        if enemyfly_hits:
            self.playerDead = True
        # checks if a player hits a platform
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

    def coin_collisions(self):
        # if player hits coin
        coin_hits = pygame.sprite.spritecollide(self.player, self.coin, True)
        for chits in coin_hits:
            if chits.type == "goldcoin":
                self.highscore.score += 300
            if chits.type == "silvercoin":
                self.highscore.score += 200
            if chits.type == "bronzecoin":
                self.highscore.score += 100

    def moving_camera(self):
        # if player reaches top of the screen move the camera
        if self.player.rect.top <= display_height / 4:
            from random import randrange
            if randrange(100) < 10:
                from Cloud import Cloud
                Cloud(self)
            self.player.position.y += max(abs(self.player.velocity.y), 2)
            # move clouds down half of the player speed
            for cloud in self.clouds:
                cloudspeed = randrange(1, 3)
                cloud.rect.y += max(abs(self.player.velocity.y / cloudspeed), 2)
            # move EnemyFly down based on player speed
            for enemyfly in self.enemyFly:
                enemyfly.rect.y += max(abs(self.player.velocity.y), 2)
            # move platforms down based on player speed
            for plat in self.platforms:
                plat.rect.y += max(abs(self.player.velocity.y), 2)
                if plat.rect.top >= display_height:
                    plat.kill()
                    self.highscore.score += 10

    def player_death(self):
        # player death
        if not self.player.tutorial:
            if self.player.rect.bottom > display_height:
                for sprite in self.all_sprites:
                    sprite.rect.y -= max(self.player.velocity.y, 7)
                    if sprite.rect.bottom < 0:
                        sprite.kill()
                        self.playerDead = True
        elif self.player.tutorial:
            if self.player.rect.bottom > display_height:
                for sprite in self.all_sprites:
                    if sprite.rect.bottom < 0:
                        self.player.position = vector2(100, 530)

if __name__ == "__main__":
    Game()
    MainMenu().game_intro()
    quit()



