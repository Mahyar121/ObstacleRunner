from ControlsPage import *
from Settings import *
import Player

class MainMenu:
    def __init__(self):
        self.bigMainText = pygame.font.Font(FONTNAME, 60)

    def gameIntroButton(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # Quit button
        if 275 + 260 > mouse[0] > 275 and 505 + 50 > mouse[1] > 505:
            Buttons().buttonBorder(white, 270, 500, 270, 60)
            Buttons().buttonBorder(pink, 275, 505, 260, 50)
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            Buttons().buttonBorder(white, 270, 500, 270, 60)
            Buttons().buttonBorder(red, 275, 505, 260, 50)
        Buttons().textButton("Quit", 275, 505, 260, 50)
        # HighScores button
        if 275 + 260 > mouse[0] > 275 and 405 + 50 > mouse[1] > 405:
            Buttons().buttonBorder(white, 270, 400, 270, 60)
            Buttons().buttonBorder(pink, 275, 405, 260, 50)
            if click[0] == 1:
                from HighScores import HighScores
                HighScores().highScoresPage()
        else:
            Buttons().buttonBorder(white, 270, 400, 270, 60)
            Buttons().buttonBorder(red, 275, 405, 260, 50)
        Buttons().textButton("High Scores", 275, 405, 260, 50)
        # Controls button
        if 275 + 260 > mouse[0] > 275 and 305 + 50 > mouse[1] > 305:
            Buttons().buttonBorder(white, 270, 300, 270, 60)
            Buttons().buttonBorder(pink, 275, 305, 260, 50)
            if click[0] == 1:
                ControlsPage().controlsPage()
        else:
            Buttons().buttonBorder(white, 270, 300, 270, 60)
            Buttons().buttonBorder(red, 275, 305, 260, 50)
        Buttons().textButton("Controls", 275, 305, 260, 50)
        # Tutorial button
        if 275 + 260 > mouse[0] > 275 and 205 + 50 > mouse[1] > 205:
            Buttons().buttonBorder(white, 270, 200, 270, 60)
            Buttons().buttonBorder(pink, 275, 205, 260, 50)
            if click[0] == 1:
                from game import Game
                # fades out the sound
                self.background_sound.fadeout(500)
                Game().tutorialPage()
        else:
            Buttons().buttonBorder(white, 270, 200, 270, 60)
            Buttons().buttonBorder(red, 275, 205, 260, 50)
        Buttons().textButton("Tutorial", 275, 205, 260, 50)
        # Play button
        if 275 + 260 > mouse[0] > 275 and 105 + 50 > mouse[1] > 105:
            Buttons().buttonBorder(white, 270, 100, 270, 60)
            Buttons().buttonBorder(pink, 275, 105, 260, 50)
            if click[0] == 1:
                from game import Game
                Game().new()
              #self.gameDifficulty()
        else:
            Buttons().buttonBorder(white, 270, 100, 270, 60)
            Buttons().buttonBorder(red, 275, 105, 260, 50)
        Buttons().textButton("Play", 275, 105, 260, 50)

    def game_intro(self):
        intro = True
        # initializes the sound
        self.background_sound = pygame.mixer.Sound("kirbytheme.ogg")
        # sets the volume from range 0.0 - 1.0
        self.background_sound.set_volume(0.2)
        # allows for endless looping!
        self.background_sound.play(loops=-1)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # background screen color
            screen.fill(teal)
            bigText = pygame.font.Font(FONTNAME, 60)
            screen.blit(pygame.font.Font(FONTNAME, 60).render(title, -1, black), (108, 12))
            textSurface, textRectange = Buttons().text_objects(title, bigText)
            textRectange.center = ((display_width / 2), (display_height / 15))
            screen.blit(textSurface, textRectange)
            # shows the buttons on the game menu screen
            self.gameIntroButton()
            pygame.display.update()
            clock.tick(FPS)
