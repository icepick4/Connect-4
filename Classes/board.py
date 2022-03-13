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
        for i in range(game.rows):
            for j in range(game.columns):
                if pawns[i][j] == 1:
                    pygame.draw.circle(self.screen, (255,60,60), (self.x + j * self.x + self.x /2,self.y + i * self.y + self.y /2), 50)
                elif pawns[i][j] == 2:
                    pygame.draw.circle(self.screen, (255,215,0), (self.x + j * self.x + self.x /2,self.y + i * self.y + self.y /2), 50)          
            #draw a pawn

    def inBoard(self,click):
        return self.x <= click[0] < self.x * 8 and self.y <= click[1] < self.y * 7

    def seePawn(self, col, game, color):
        ctr = -1
        for i in range(game.rows):
            if game.grid[i][col] == 0:
                ctr+=1
        pygame.draw.circle(self.screen, color, (self.x + col * self.x + self.x /2,self.y + ctr * self.y + self.y /2), 50)

