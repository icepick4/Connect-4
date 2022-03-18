import pygame
from variables import RED, YELLOW, BORDERRED, BORDERYELLOW, BLACK, GREY, caseW, caseH

class Board:
    def __init__(self, width, height, screen):
        self.screen = screen
        self.drawBoard()
        pygame.draw.line(self.screen, BLACK, (0,caseH * 8 - 2), (caseW * 9 + 20, caseH * 8 - 2), 12)

    def drawBoard(self):
        #vertical
        for i in range(8):
            pygame.draw.line(self.screen, BLACK, (caseW + i * caseW + 2, caseH *2), (caseW + i * caseW + 2, caseH * 8), 2)
            pygame.draw.line(self.screen, GREY, (caseW + i * caseW, caseH*2), (caseW + i * caseW, caseH * 8), 4)
            pygame.draw.line(self.screen, BLACK, (caseW + i * caseW - 2, caseH*2), (caseW + i * caseW - 2, caseH * 8), 2)
        #horizontal
        for i in range(7):
            pygame.draw.line(self.screen, BLACK, (caseW, caseH *2 + i * caseH + 2), (caseW * 9 - caseW, caseH *2 + i * caseH + 2), 2)
            pygame.draw.line(self.screen, GREY, (caseW, caseH *2+ i * caseH), (caseW * 9 - caseW, caseH *2 + i * caseH), 4)
            pygame.draw.line(self.screen, BLACK, (caseW, caseH *2 + i * caseH - 2), (caseW * 9 - caseW, caseH *2 + i * caseH - 2), 2)


    def inBoard(self,click):
        #check pos mouse in board
        return caseW <= click[0] < caseW * 8 and caseH <= click[1] < caseH * 7

    def seePawn(self, col, color):
        if color == RED:
            borderColor = BORDERRED
        else:
            borderColor = BORDERYELLOW
        pygame.draw.circle(self.screen, borderColor, (caseW + col * caseW + caseW /2,caseH*2 + -1 * caseH + caseH /2), (caseW / 4) + 5, 5)
        pygame.draw.circle(self.screen, color, (caseW + col * caseW + caseW /2,caseH*2 + -1 * caseH + caseH /2), caseW / 4)
        

