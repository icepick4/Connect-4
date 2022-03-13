import pygame

class Text:
    def __init__(self, screen, text, font, pos, type):
        self.screen = screen
        self.text = text
        self.font = font
        if type == "red":
            self.color = (255,0,0)
        elif type == "yellow":
            self.color = (255,255,0)
        else:
            self.color = (0,0,0)
        self.pos = pos
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect(midbottom=self.pos)

    def display(self):
        self.screen.blit(self.surface,self.rect)
