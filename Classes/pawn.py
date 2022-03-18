import pygame

class Pawn:
    def __init__(self, pos, color, width, height):
        self.pos = pos
        self.color = color
        self.surface = pygame.Surface((width, height))
        self.rect = self.surface.get_rect(topleft = (pos[0] * width, height / 2, ))
        pygame.draw.circle(self.surface, color, (0,0), width / 2)
        #last pos : (width + pos[1] * width + width /2,height*2 + pos[0] * height + height /2)
