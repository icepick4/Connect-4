import pygame

class Pawn:
    def __init__(self, pos, color, borderColor, width, height):
        self.lastRow = pos[1]
        self.col = pos[0]
        self.posYAnimation = -1
        self.width = width 
        self.height = height 
        self.color = color
        self.borderColor = borderColor
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
        self.surface = self.surface.convert_alpha()
        pygame.draw.circle(self.surface, color, (width / 2,height / 2), self.width / 4)
        pygame.draw.circle(self.surface, borderColor, (width / 2,height / 2), (self.width / 4) + 5, 5)

    def animation(self, screen):
        #new pos
        self.rect = self.surface.get_rect(midtop = (self.width + self.col * self.width + self.width /2, self.height*2 + self.posYAnimation * self.height - 5))
        #while new row not reached -> posY grows
        if self.posYAnimation < self.lastRow:
            self.posYAnimation += 0.05
            inMove = True
        else:
            inMove = False
        screen.blit(self.surface, self.rect)
        #return the state to let the pawns move while the game's won
        return inMove

