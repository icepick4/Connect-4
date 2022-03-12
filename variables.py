import pygame       
pygame.init()

windowSize = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode(windowSize)
width = windowSize[0]
height = windowSize[1]

fontPath = "assets/font/leaguespartan-bold.ttf"

playing = True

#bouton pour fermer la fenetre
endFont = pygame.font.Font(fontPath, 50)
endSurface = endFont.render("CLOSE", True, (0,0,0))
endRect = endSurface.get_rect(topright=(width - 10,10))