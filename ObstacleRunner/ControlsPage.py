from Buttons import *
from Settings import *
'''
Mahyar Haji Babaie
mahyarhajibabaie@csu.fullerton.edu

Michael Franzen
mfranzen15@gmail.com

This file loads the control page for the user
'''

class ControlsPage:
    def __init__(self):
        self.bigText = pygame.font.Font(FONTNAME, 50)

    def controlButtons(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # quit button
        if 480 + 300 > mouse[0] > 480 and 545 + 40 > mouse[1] > 545:
            Buttons().buttonBorder(white, 475, 540, 310, 50)
            Buttons().buttonBorder(pink, 480, 545, 300, 40)
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            Buttons().buttonBorder(white, 475, 540, 310, 50)
            Buttons().buttonBorder(red, 480, 545, 300, 40)
        Buttons().textButton("Quit", 480, 545, 300, 40)
        # back button
        if 80 + 280 > mouse[0] > 80 and 545 + 40 > mouse[1] > 545:
            Buttons().buttonBorder(white, 75, 540, 290, 50)
            Buttons().buttonBorder(pink, 80, 545, 280, 40)
            if click[0] == 1:
                from MainMenu import MainMenu
                MainMenu().game_intro()
        else:
            Buttons().buttonBorder(white, 75, 540, 290, 50)
            Buttons().buttonBorder(red, 80, 545, 280, 40)
        Buttons().textButton("Back", 80, 545, 280, 40)
        # Control BUTTONS
        # Move Left
        Buttons().buttonBorder(orange, 75, 125, 290, 50)
        Buttons().buttonBorder(red, 80, 130, 280, 40)
        Buttons().textButton("Move Left:", 80, 130, 280, 40)
        # left arrow
        Buttons().buttonBorder(orange, 475, 125, 310, 50)
        Buttons().buttonBorder(red, 480, 130, 300, 40)
        Buttons().textButton("Left Arrow or A", 480, 130, 300, 40)
        # Move Right
        Buttons().buttonBorder(orange, 75, 195, 290, 50)
        Buttons().buttonBorder(red, 80, 200, 280, 40)
        Buttons().textButton("Move Right:", 80, 200, 280, 40)
        # right arrow
        Buttons().buttonBorder(orange, 475, 195, 310, 50)
        Buttons().buttonBorder(red, 480, 200, 300, 40)
        Buttons().textButton("Right Arrow or D", 480, 200, 300, 40)
        # Move Up
        Buttons().buttonBorder(orange, 75, 265, 290, 50)
        Buttons().buttonBorder(red, 80, 270, 280, 40)
        Buttons().textButton("Jump:", 80, 270, 280, 40)
        # up arrow
        Buttons().buttonBorder(orange, 475, 265, 310, 50)
        Buttons().buttonBorder(red, 480, 270, 300, 40)
        Buttons().textButton("SpaceBar", 480, 270, 300, 40)
        # Move Down
        Buttons().buttonBorder(orange, 75, 335, 290, 50)
        Buttons().buttonBorder(red, 80, 340, 280, 40)
        Buttons().textButton("Punch:", 80, 340, 280, 40)
        # down arrow
        Buttons().buttonBorder(orange, 475, 335, 310, 50)
        Buttons().buttonBorder(red, 480, 340, 300, 40)
        Buttons().textButton("F", 480, 340, 300, 40)
        # Shoot
        Buttons().buttonBorder(orange, 75, 405, 290, 50)
        Buttons().buttonBorder(red, 80, 410, 280, 40)
        Buttons().textButton("Kick:", 80, 410, 280, 40)
        # Space Bar
        Buttons().buttonBorder(orange, 475, 405, 310, 50)
        Buttons().buttonBorder(red, 480, 410, 300, 40)
        Buttons().textButton("G", 480, 410, 300, 40)


    def controlsPage(self):
        controls = True
        while controls:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            # fills screen
            screen.fill(teal)
            screen.blit(pygame.font.Font(FONTNAME, 50).render(title, -1, black), (153, 17))
            textSurface, textRectange = Buttons().text_objects(title, self.bigText)
            textRectange.center = ((display_width / 2), (display_height / 15))
            screen.blit(textSurface, textRectange)

            screen.blit(pygame.font.Font(FONTNAME, 40).render("Controls Page", -1, white), (232, 71))
            screen.blit(pygame.font.Font(FONTNAME, 40).render("Controls Page", -1, red), (230, 70))


            self.controlButtons()
            pygame.display.update()
            clock.tick(FPS)
