'''
Mahyar Haji Babaie
mahyarhajibabaie@csu.fullerton.edu

Michael Franzen
mfranzen15@gmail.com

This file generates button images and borders
'''
from Settings import *


# handles the text and buttons
class Buttons:
    def __init__(self):
        pygame.font.init()
        self.smallText = pygame.font.Font(FONTNAME, 30)

    # makes the text
    def text_objects(self, text, font):
        # white font
        textSurface = font.render(text, True, white)
        return textSurface, textSurface.get_rect()

    # makes the button border
    def buttonBorder(self, color, x, y, w, h):
        pygame.draw.rect(screen, color, (x, y, w, h))

    # used for text for button border
    def textButton(self, txt, x, y, w, h, ):
        textSurface, textRectangle = self.text_objects(txt, self.smallText)
        textRectangle.center = ((x + (w / 2)), (y + (h / 2)))
        screen.blit(textSurface, textRectangle)