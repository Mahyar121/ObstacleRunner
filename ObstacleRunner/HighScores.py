
from pygame.locals import *
from Buttons import *
import json


class HighScores:

    def __init__(self, userName, highScoreList):
        self.fileName = "HighScore.json"
        self.userName = userName
        self.highScoreList = highScoreList
        self.fontName = FONTNAME
        self.score = 0

    def highScoresPage(self):
        padding_y = 0
        maxScores = 8  # We *could* paint every score, but it's not any good if you can't see them (because we run out of the screen).
        scoresCount = 1
        highScore = True
        screen.fill(black)
        with open(self.fileName) as highscore_file:
            self.highScoreList = json.load(highscore_file)
        while highScore:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            for score in self.highScoreList:
                if scoresCount <= maxScores and scoresCount <= len(self.highScoreList):
                    screen.blit(
                        pygame.font.Font(self.fontName, 50).render(
                            str(scoresCount) + ".  " + str(score["name"]) + ": " + str(score["score"]), 1,
                            white), (250, 140 + padding_y))
                    padding_y += 50
                    scoresCount += 1

            bigText = pygame.font.Font(self.fontName, 60)
            textSurface, textRectange = Buttons().text_objects(title, bigText)
            textRectange.center = ((display_width / 2), (display_height / 15))
            screen.blit(textSurface, textRectange)

            line = "_____________________________________________________________________"
            screen.blit(pygame.font.Font(self.fontName, 50).render(line, -1, green), (0, 80))
            screen.blit(pygame.font.Font(self.fontName, 50).render("High Scores", -1, brightGreen),(270, 70))

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            # quit button
            if 505 + 280 > mouse[0] > 505 and 545 + 40 > mouse[1] > 545:
                Buttons().buttonBorder(white, 500, 540, 290, 50)
                Buttons().buttonBorder(brightGreen, 505, 545, 280, 40)
                if click[0] == 1:
                    pygame.quit()
                    quit()
            else:
                Buttons().buttonBorder(white, 500, 540, 290, 50)
                Buttons().buttonBorder(green, 505, 545, 280, 40)
            Buttons().textButton("Quit", 505, 545, 280, 40)
            # back button
            if 25 + 280 > mouse[0] > 25 and 545 + 40 > mouse[1] > 545:
                Buttons().buttonBorder(white, 20, 540, 290, 50)
                Buttons().buttonBorder(brightGreen, 25, 545, 280, 40)
                if click[0] == 1:
                    from MainMenu import MainMenu
                    MainMenu().game_intro()
            else:
                Buttons().buttonBorder(white, 20, 540, 290, 50)
                Buttons().buttonBorder(green, 25, 545, 280, 40)
            Buttons().textButton("Back", 25, 545, 280, 40)
            pygame.display.update()

    def addHighScores(self):
        with open(self.fileName) as highscore_file:
            self.highScoreList = json.load(highscore_file)

        if not self.highScoreList == None:  # Make sure the prev. scores are loaded.
            new_json_score = {  # Create a JSON-object with the score, name
                "name": self.userName,
                "score": self.score,
            }
            self.highScoreList.append(new_json_score)  # Add the score to the list of scores.

            self.highScoreList = self.sortHighScores(self.highScoreList)  # Sort the scores.

            highscore_file = open(self.fileName, "w")
            highscore_file.write(json.dumps(self.highScoreList))  # Save the list of scores to highscore.json

    def sortHighScores(self, json):
        scores_dict = dict()  # Create a dictionary object.
        sorted_list = list()  # Create a list object.

        for obj in json:
            scores_dict[
                # Add every score to a dictionary with its score as key.
                obj["score"]] = obj
        # Read the sorted dictionary in reverse order (highest score first)...
        for key in sorted(scores_dict.keys(),reverse=True):
            sorted_list.append(scores_dict[key])  # ...and add it to a list.

        return sorted_list  # Returns a sorted list.

    def getUserName(self):
        loop = True
        while loop:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.unicode.isalpha():
                        self.userName += event.unicode
                    elif event.key == K_BACKSPACE:
                        self.userName = self.userName[:-1]
                    elif event.key == K_RETURN:
                        self.addHighScores()
                        loop = False
                elif event.type == QUIT:
                    pygame.quit()
                    quit()
            screen.blit(pygame.font.Font(self.fontName, 50).render(self.userName, -1, white), (100, 500))
            pygame.display.update()
