
from pygame.locals import *
from Buttons import *
import json


# handles the high scores
class HighScores:
    def __init__(self):
        self.fileName = "HighScore.json"
        self.userName = ""
        self.highScoreList = []
        self.fontName = FONTNAME
        self.score = 0
        self.namebackground = ""

    def highScoresPage(self):
        padding_y = 0
        maxScores = 7
        scoresCount = 1
        highScore = True
        screen.fill(teal)
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
                            white), (200, 140 + padding_y))
                    padding_y += 50
                    scoresCount += 1

            bigText = pygame.font.Font(self.fontName, 60)
            screen.blit(pygame.font.Font(FONTNAME, 60).render(title, -1, black), (107, 13))
            textSurface, textRectange = Buttons().text_objects(title, bigText)
            textRectange.center = ((display_width / 2), (display_height / 15))
            screen.blit(textSurface, textRectange)

            line = "_____________________________________________________________________"
            screen.blit(pygame.font.Font(self.fontName, 50).render(line, -1, white), (0, 81))
            screen.blit(pygame.font.Font(self.fontName, 50).render(line, -1, red), (0, 80))
            screen.blit(pygame.font.Font(self.fontName, 50).render("High Scores", -1, white), (272, 73))
            screen.blit(pygame.font.Font(self.fontName, 50).render("High Scores", -1, red),(270, 70))

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            # quit button
            if 505 + 280 > mouse[0] > 505 and 545 + 40 > mouse[1] > 545:
                Buttons().buttonBorder(white, 500, 540, 290, 50)
                Buttons().buttonBorder(pink, 505, 545, 280, 40)
                if click[0] == 1:
                    pygame.quit()
                    quit()
            else:
                Buttons().buttonBorder(white, 500, 540, 290, 50)
                Buttons().buttonBorder(red, 505, 545, 280, 40)
            Buttons().textButton("Quit", 505, 545, 280, 40)
            # back button
            if 25 + 280 > mouse[0] > 25 and 545 + 40 > mouse[1] > 545:
                Buttons().buttonBorder(white, 20, 540, 290, 50)
                Buttons().buttonBorder(pink, 25, 545, 280, 40)
                if click[0] == 1:
                    from MainMenu import MainMenu
                    MainMenu().game_intro()
            else:
                Buttons().buttonBorder(white, 20, 540, 290, 50)
                Buttons().buttonBorder(red, 25, 545, 280, 40)
            Buttons().textButton("Back", 25, 545, 280, 40)
            pygame.display.update()

    def addHighScores(self, score):
        self.score = score
        with open(self.fileName) as highscore_file:
            self.highScoreList = json.load(highscore_file)

        if self.highScoreList:  # Make sure the prev. scores are loaded.
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
        for key in sorted(scores_dict.keys(), reverse=True):
            sorted_list.append(scores_dict[key])  # ...and add it to a list.

        return sorted_list  # Returns a sorted list.

    def getUserName(self, score):
        self.score = score

        loop = True
        while loop:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.unicode.isalpha():
                        self.userName += event.unicode
                        self.namebackground += event.unicode
                    if event.key == K_BACKSPACE:
                        self.userName = self.userName[:-1]
                        self.namebackground = self.namebackground[:-1]
                    if event.key == K_RETURN:
                        self.addHighScores(self.score)
                        loop = False
                elif event.type == QUIT:
                    pygame.quit()
                    quit()
            screen.blit(pygame.font.Font(self.fontName, 50).render(self.userName, -1, black), (100, 500))
            screen.blit(pygame.font.Font(self.fontName, 50).render(self.namebackground, -1, white), (101, 502))
            pygame.display.update()

