
from Settings import *


class Buttons:
    def __init__(self):
        pygame.font.init()
        self.smallText = pygame.font.Font(FONTNAME, 30)

    def text_objects(self, text, font):
        # white font
        textSurface = font.render(text, True, white)
        return textSurface, textSurface.get_rect()

    def buttonBorder(self, color, x, y, w, h):
        pygame.draw.rect(screen, color, (x, y, w, h))

    def textButton(self, txt, x, y, w, h, ):
        textSurface, textRectangle = self.text_objects(txt, self.smallText)
        textRectangle.center = ((x + (w / 2)), (y + (h / 2)))
        screen.blit(textSurface, textRectangle)