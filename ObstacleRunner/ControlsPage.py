from Buttons import *
from Settings import *


class ControlsPage:
    def __init__(self):
        self.bigText = pygame.font.Font(FONTNAME, 50)

    def controlButtons(self):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # quit button
        if 480 + 260 > mouse[0] > 480 and 545 + 40 > mouse[1] > 545:
            Buttons().buttonBorder(white, 475, 540, 290, 50)
            Buttons().buttonBorder(brightGreen, 480, 545, 280, 40)
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            Buttons().buttonBorder(white, 475, 540, 290, 50)
            Buttons().buttonBorder(green, 480, 545, 280, 40)
        Buttons().textButton("Quit", 480, 545, 280, 40)
        # back button
        if 80 + 260 > mouse[0] > 80 and 545 + 40 > mouse[1] > 545:
            Buttons().buttonBorder(white, 75, 540, 290, 50)
            Buttons().buttonBorder(brightGreen, 80, 545, 280, 40)
            if click[0] == 1:
                from MainMenu import MainMenu
                MainMenu().game_intro()
        else:
            Buttons().buttonBorder(white, 75, 540, 290, 50)
            Buttons().buttonBorder(green, 80, 545, 280, 40)
        Buttons().textButton("Back", 80, 545, 280, 40)
        # Control BUTTONS
        # Move Left
        Buttons().buttonBorder(red, 75, 125, 290, 50)
        Buttons().buttonBorder(teal, 80, 130, 280, 40)
        Buttons().textButton("Move Left:", 80, 130, 280, 40)
        # left arrow
        Buttons().buttonBorder(red, 475, 125, 290, 50)
        Buttons().buttonBorder(teal, 480, 130, 280, 40)
        Buttons().textButton("Left Arrow or A", 480, 130, 280, 40)
        # Move Right
        Buttons().buttonBorder(red, 75, 195, 290, 50)
        Buttons().buttonBorder(teal, 80, 200, 280, 40)
        Buttons().textButton("Move Right:", 80, 200, 280, 40)
        # right arrow
        Buttons().buttonBorder(red, 475, 195, 290, 50)
        Buttons().buttonBorder(teal, 480, 200, 280, 40)
        Buttons().textButton("Right Arrow or D", 480, 200, 280, 40)
        # Move Up
        Buttons().buttonBorder(red, 75, 265, 290, 50)
        Buttons().buttonBorder(teal, 80, 270, 280, 40)
        Buttons().textButton("Move Up:", 80, 270, 280, 40)
        # up arrow
        Buttons().buttonBorder(red, 475, 265, 290, 50)
        Buttons().buttonBorder(teal, 480, 270, 280, 40)
        Buttons().textButton("Up Arrow or W", 480, 270, 280, 40)
        # Move Down
        Buttons().buttonBorder(red, 75, 335, 290, 50)
        Buttons().buttonBorder(teal, 80, 340, 280, 40)
        Buttons().textButton("Move Down:", 80, 340, 280, 40)
        # down arrow
        Buttons().buttonBorder(red, 475, 335, 290, 50)
        Buttons().buttonBorder(teal, 480, 340, 280, 40)
        Buttons().textButton("Down Arrow or S", 480, 340, 280, 40)
        # Shoot
        Buttons().buttonBorder(red, 75, 405, 290, 50)
        Buttons().buttonBorder(teal, 80, 410, 280, 40)
        Buttons().textButton("Shoot:", 80, 410, 280, 40)
        # Space Bar
        Buttons().buttonBorder(red, 475, 405, 290, 50)
        Buttons().buttonBorder(teal, 480, 410, 280, 40)
        Buttons().textButton("SpaceBar", 480, 410, 280, 40)
        # Bomb
        Buttons().buttonBorder(red, 75, 475, 290, 50)
        Buttons().buttonBorder(teal, 80, 480, 280, 40)
        Buttons().textButton("Bomb:", 80, 480, 280, 40)
        # B
        Buttons().buttonBorder(red, 475, 475, 290, 50)
        Buttons().buttonBorder(teal, 480, 480, 280, 40)
        Buttons().textButton("B", 480, 480, 280, 40)

    def controlsPage(self):
        controls = True
        while controls:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            # black screen
            screen.fill(black)
            textSurface, textRectange = Buttons().text_objects(title, self.bigText)
            textRectange.center = ((display_width / 2), (display_height / 15))
            screen.blit(textSurface, textRectange)

            screen.blit(pygame.font.Font(FONTNAME, 40).render("Controls Page", -1, brightGreen), (230, 70))

            self.controlButtons()
            pygame.display.update()
            clock.tick(FPS)
