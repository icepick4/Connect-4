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
            pygame.draw.line(self.screen, (0,0,0), (self.x + i * self.x + 2, self.y), (self.x + i * self.x + 2, self.y * 8 - self.y), 2)
            pygame.draw.line(self.screen, (50,50,50), (self.x + i * self.x, self.y), (self.x + i * self.x, self.y * 8 - self.y), 4)
            pygame.draw.line(self.screen, (0,0,0), (self.x + i * self.x - 2, self.y), (self.x + i * self.x - 2, self.y * 8 - self.y), 2)
        #horizontal
        for i in range(7):
            pygame.draw.line(self.screen, (0,0,0), (self.x, self.y + i * self.y + 2), (self.x * 9 - self.x, self.y + i * self.y + 2), 2)
            pygame.draw.line(self.screen, (50,50,50), (self.x, self.y + i * self.y), (self.x * 9 - self.x, self.y + i * self.y), 4)
            pygame.draw.line(self.screen, (0,0,0), (self.x, self.y + i * self.y - 2), (self.x * 9 - self.x, self.y + i * self.y - 2), 2)

    def drawPawn(self, game):
        pawns = game.grid
        for i in range(game.rows):
            for j in range(game.columns):
                if pawns[i][j] == 1:
                    pygame.draw.circle(self.screen, (200,0,0), (self.x + j * self.x + self.x /2,self.y + i * self.y + self.y /2), (self.x / 4) + 5, 5)
                    pygame.draw.circle(self.screen, (255,50,50), (self.x + j * self.x + self.x /2,self.y + i * self.y + self.y /2),self.x / 4)
                elif pawns[i][j] == 2:
                    pygame.draw.circle(self.screen, (160,150,5), (self.x + j * self.x + self.x /2,self.y + i * self.y + self.y /2), (self.x / 4) + 5, 5)
                    pygame.draw.circle(self.screen, (255,215,0), (self.x + j * self.x + self.x /2,self.y + i * self.y + self.y /2), self.x / 4)          
            #draw a pawn

    def inBoard(self,click):
        #check pos mouse in board
        return self.x <= click[0] < self.x * 8 and self.y <= click[1] < self.y * 7

    def seePawn(self, col, game, color):
        ctr = -1
        for i in range(game.rows):
            if game.grid[i][col] == 0:
                ctr+=1
        if color == (255,50,50):
            borderColor = (200,0,0)
        else:
            borderColor = (160,150,5)
        pygame.draw.circle(self.screen, borderColor, (self.x + col * self.x + self.x /2,self.y + ctr * self.y + self.y /2), (self.x / 4) + 5, 5)
        pygame.draw.circle(self.screen, color, (self.x + col * self.x + self.x /2,self.y + ctr * self.y + self.y /2), self.x / 4)

