import pygame
from variables import RED, YELLOW, BORDERRED, BORDERYELLOW, BLACK, GREY

class Board:
    def __init__(self, width, height, screen):
        self.x = width // 9
        self.y = height // 8
        self.screen = screen
        self.drawBoard()
        pygame.draw.line(self.screen, BLACK, (0,self.y * 8 - 2), (self.x * 9 + 20, self.y * 8 - 2), 12)

    def drawBoard(self):
        #vertical
        for i in range(8):
            pygame.draw.line(self.screen, BLACK, (self.x + i * self.x + 2, self.y *2), (self.x + i * self.x + 2, self.y * 7.95), 2)
            pygame.draw.line(self.screen, GREY, (self.x + i * self.x, self.y*2), (self.x + i * self.x, self.y * 7.95), 4)
            pygame.draw.line(self.screen, BLACK, (self.x + i * self.x - 2, self.y*2), (self.x + i * self.x - 2, self.y * 7.95), 2)
        #horizontal
        for i in range(7):
            pygame.draw.line(self.screen, BLACK, (self.x, self.y *2 + i * self.y + 2), (self.x * 9 - self.x, self.y *2 + i * self.y + 2), 2)
            pygame.draw.line(self.screen, GREY, (self.x, self.y *2+ i * self.y), (self.x * 9 - self.x, self.y *2 + i * self.y), 4)
            pygame.draw.line(self.screen, BLACK, (self.x, self.y *2 + i * self.y - 2), (self.x * 9 - self.x, self.y *2 + i * self.y - 2), 2)

    def inBoard(self,click):
        #check pos mouse in board
        return self.x <= click[0] < self.x * 8 and self.y <= click[1] < self.y * 7

    def seePawn(self, col, color):
        if color == RED:
            borderColor = BORDERRED
        else:
            borderColor = BORDERYELLOW
        pygame.draw.circle(self.screen, borderColor, (self.x + col * self.x + self.x /2,self.y*2 + -1 * self.y + self.y /2), (self.x / 4) + 5, 5)
        pygame.draw.circle(self.screen, color, (self.x + col * self.x + self.x /2,self.y*2 + -1 * self.y + self.y /2), self.x / 4)
        

