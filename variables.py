from Classes.game import Game
from Classes.text import Text
import pygame       
pygame.init()
windowSize = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode(windowSize)
width = windowSize[0]
height = windowSize[1]

fontPath = "assets/font/leaguespartan-bold.ttf"
font = pygame.font.Font(fontPath, 50)
littleFont = pygame.font.Font(fontPath, 43)
playing = True
player = 1
#bouton pour fermer la fenetre

endSurface = font.render("CLOSE", True, (0,0,0))
endRect = endSurface.get_rect(topright=(width - 10,10))

inGame = False

centeredPos = (width/2, height /13)
redTurn = Text(screen, "Red's turn !", font, centeredPos, "red")
yellowTurn = Text(screen, "Yellow's turn !", font, centeredPos, "yellow")
winRed = Text(screen, "Red won !", font, centeredPos, "red")
winYellow = Text(screen, "Yellow won !", font, centeredPos, "yellow")
newGame = Text(screen, "Click anywhere to start a new game !", littleFont, (width/2, height / 8), "black")
game = Game()
