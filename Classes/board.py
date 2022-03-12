import pygame

class Board:
    def __init__(self, width, height, screen):
        self.x = width // 9
        self.y = height // 8
        self.screen = screen
        self.drawBoard()

    def drawBoard(self):
        #vertical
        for i in range(8):
            pygame.draw.line(self.screen, (0,0,0), (self.x + i * self.x, self.y), (self.x + i * self.x, self.y * 8 - self.y), 5)
        #horizontal
        for i in range(7):
            pygame.draw.line(self.screen, (0,0,0), (self.x, self.y + i * self.y), (self.x * 9 - self.x, self.y + i * self.y), 5)
    
    def drawPawn(self, game):
        pawns = game.grid
        for i,line in enumerate(pawns):
            if line[i] == 1:
                #draw red
                pass
            elif line[i] == 2:
                #draw yellow
                pass
            #draw a pawn
        pass

    def inBoard(self,click):
        return self.x <= click[0] < self.x * 8 and self.y <= click[1] < self.y * 7

