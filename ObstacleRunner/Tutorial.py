
from Settings import *


class Tutorial:

    def __init__(self):
        self.font = pygame.font.Font(FONTNAME, 25)

    def tutorialPage(self):
        bombTimer = 20
        fpsCount = 0
        seconds = 5
        mainmenuSeconds = 0
        key = pygame.key.get_pressed()
        clock = pygame.time.Clock()
        tutorialCount = 0
        tutorialFPScount = 0
        FPS = 60
        left = False
        right = False
        up = False
        down = False
        fire = False
        bomb = False
        tutorialExit = False
        bigFont = pygame.font.Font(FONTNAME, 40)
        medFont = pygame.font.Font(FONTNAME, 30)
        while not tutorialExit:
            clock.tick(FPS)
            screen.fill(black)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            screen.blit(
                pygame.font.Font(FONTNAME, 23).render("Type q to exit tutorial", -1, self.brightGreen),
                (222, 10))
            screen.blit(self.player, (self.playerPosX, self.playerPosY))
            key = pygame.key.get_pressed()
            if key[K_LEFT] or key[K_a] and self.playerPosX > 0:
                self.playerPosX -= 5
                left = True
            if (key[K_RIGHT] or key[K_d]) and self.playerPosX < display_width - self.player.get_width() and left:
                self.playerPosX += 5
                right = True
            if (key[K_UP] or key[K_w]) and left and right and self.playerPosY > 0:
                self.playerPosY -= 5
                up = True
            if (key[K_DOWN] or key[
                K_s]) and left and right and up and self.playerPosY < display_height - self.player.get_height():
                self.playerPosY += 5
                down = True
            if key[K_SPACE] and left and right and up and down and not self.bullet:
                fire = True
                self.bullet = pygame.Rect(self.playerPosX + self.player.get_width() / 4, self.playerPosY - 15, 5, 10)
            if key[K_b] and left and right and up and down and fire and not self.bomb and self.bombCount > 0:
                bomb = True
                self.bomb = screen.blit(self.bomb1,
                                             (self.playerPosX + self.player.get_width() / 4, self.playerPosY - 15))
            if key[K_q]:
                self.playAgain()
                from MainMenu import MainMenu
                MainMenu().game_intro()

            if not left:
                screen.blit(bigFont.render("Press A or Left Arrow to move left", -1, red), (10, 40))
            if left and not right and not up and not down and not fire and not bomb:
                screen.blit(bigFont.render("Press D or Right Arrow to move right", -1, teal), (10, 40))
            if left and right and not up and not down and not fire and not bomb:
                screen.blit(bigFont.render("Press W or Up Arrow to move up", -1, brightGreen), (10, 40))
            if left and right and up and not down and not fire and not bomb:
                screen.blit(bigFont.render("Press S or Down Arrow to move down", -1, yellow), (10, 40))
            if left and right and up and down and not fire and not bomb:
                screen.blit(bigFont.render("Press Spacebar to fire", -1, orange), (10, 40))
            if left and right and up and down and fire and not bomb:
                screen.blit(bigFont.render("Press B to release a bomb", -1, lightPurple), (10, 40))
            if left and right and up and down and fire and bomb and tutorialCount == 0:
                screen.blit(medFont.render("Remember you have a limited amount of bombs", -1, brightGreen),(0, 40))
                screen.blit(medFont.render("If the bomb timer equals 0 you get a new bomb", -1, red), (5, 80))
                screen.blit(medFont.render("Bombs give 0 points if it kills a target", -1, brightGreen),(15, 120))
                tutorialFPScount += 1
                if tutorialFPScount == 700:
                    tutorialCount += 1
            if tutorialCount == 1:
                screen.blit(medFont.render("You lose 100 points if you shoot at the barrier", -1, teal),(10, 40))
                screen.blit(
                    medFont.render("Game Difficulty determines how many points per kill", -1, brightOrange),(10, 80))
                screen.blit(medFont.render("Use your bombs for emergency situations", -1, orange), (10, 120))
                tutorialFPScount += 1
                if tutorialFPScount == 1400:
                    tutorialCount += 1
            if tutorialCount == 2:
                screen.blit(bigFont.render("You will lose if your lives goes down to 0", -1, yellow),(10, 40))
                screen.blit(bigFont.render("You will win if you kill all the enemies", -1, red), (10, 80))
                tutorialFPScount += 1
                if tutorialFPScount == 1900:
                    tutorialCount += 1
            if tutorialCount == 3:
                screen.blit(bigFont.render("You have completed the Tutorial!", -1, teal), (10, 40))
                screen.blit(bigFont.render("Returning to MainMenu in {}".format(seconds), -1, lightPurple),(10, 80))
                mainmenuSeconds += 1
                if mainmenuSeconds == 70:
                    mainmenuSeconds = 0
                    seconds -= 1
                if seconds == 0:
                    self.playAgain()
                    from MainMenu import MainMenu
                    MainMenu().game_intro()

            if bombTimer == 0:
                bombTimer = 20
                self.bombCount += 1
            if fpsCount == 60:
                fpsCount = 0
                bombTimer -= 1
            fpsCount += 1
            if self.bullet:
                pygame.draw.rect(screen, (52, 255, 0), self.bullet)
            if self.bomb:
                self.bombAnimation()
            self.bombUpdate()
            self.bulletUpdate()
            screen.blit(self.font.render("Lives: {}".format(self.lives), -1, white), (0, 10))
            screen.blit(self.font.render("Score: {}".format(self.score), -1, white), (450, 10))
            screen.blit(self.font.render("Bombs: {}".format(self.bombCount), -1, white), (100, 10))
            screen.blit(self.font.render("Bomb Timer: {}".format(bombTimer), -1, white), (620, 10))
            pygame.display.update()