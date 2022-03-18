from Classes.game import Game
from Classes.text import Text
import pygame  
from time import time     
pygame.init()

RED = (255,50,50)
BORDERRED = (200,0,0)
YELLOW = (255,215,0)
BORDERYELLOW = (160,150,5)
BLACK = (0,0,0)
GREY = (50,50,50)

windowSize = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode(windowSize)
width = windowSize[0]
height = windowSize[1]
caseW = width / 9
caseH = height / 8
fontPath = "assets/font/leaguespartan-bold.ttf"
font = pygame.font.Font(fontPath, 50)
littleFont = pygame.font.Font(fontPath, 43)

playing = True
player = 1
winRedCTR = 0
winYellowCTR = 0

inGame = False
inMove = False

centeredPos = (width/2, height /13)
redTurn = Text(screen, "Red's turn !", font, centeredPos, RED)
yellowTurn = Text(screen, "Yellow's turn !", font, centeredPos, YELLOW)
winRed = Text(screen, "Red won !", font, centeredPos, RED)
winYellow = Text(screen, "Yellow won !", font, centeredPos, YELLOW)
draw = Text(screen, "Draw !", font, centeredPos, BLACK)
newGame = Text(screen, "Click anywhere to start a new game !", littleFont, (width/2, height / 8), BLACK)


yellowCounterSurface = littleFont.render("yellow : {0}".format(winYellowCTR), True, (255,255,0))
yellowCounterRect = yellowCounterSurface.get_rect(topleft = (5,5))
redCounterSurface = littleFont.render("red       : {0}".format(winRedCTR), True, (255,0,0))
redCounterRect = redCounterSurface.get_rect(topleft = (5,yellowCounterRect.bottom))

cancelSurface = littleFont.render("CANCEL LAST MOVE", True, (0,0,0))
cancelRect = cancelSurface.get_rect(midbottom = (width / 2, height / 8))

#bouton pour fermer la fenetre
endSurface = font.render("CLOSE", True, (0,0,0))
endRect = endSurface.get_rect(topright=(width - 10,10))

#win sound
winSound = pygame.mixer.Sound('assets/audio/win.wav')
game = Game()
pawns = []