import pygame
from variables import caseW, caseH
class Pawn:
    def __init__(self, pos, color, borderColor, width, height):
        self.lastRow = pos[1]
        self.col = pos[0]
        self.rowAnimation = -1
        self.color = color
        self.borderColor = borderColor
        self.surface = pygame.Surface((caseW, caseH), pygame.SRCALPHA, 32)
        self.surface = self.surface.convert_alpha()

        pygame.draw.circle(self.surface, color, (width / 2,height / 2), caseW / 4)
        pygame.draw.circle(self.surface, borderColor, (width / 2,height / 2), (caseW / 4) + 5, 5)

    def animation(self, screen, speed):
        #new pos
        self.rect = self.surface.get_rect(midtop = (caseW + self.col * caseW + caseW /2, caseH*2 + self.rowAnimation * caseH - self.rowAnimation * 1))
        #while new row not reached -> row grows
        if self.rowAnimation < self.lastRow:
            self.rowAnimation += speed
            inMove = True
        else:
            inMove = False
        screen.blit(self.surface, self.rect)
        #return the state to let the pawns move while the game's won
        return inMove

