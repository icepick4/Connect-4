from variables import *
try:
    import pygame
    from pygame.locals import *
except:
    print("Vous n'avez pas téléchargé le module pygame ! \n Téléchargez le avec la commande ci-contre : pip install pygame")
from Classes.game import Game
from Classes.board import Board

game = Game()
while playing:
    screen.fill((255,255,255))
    board = Board(width, height, screen)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            #on presse le bouton close
            click = event.pos
            clickX = click[0]
            clickY = click[1]
            case = int((clickX % width // 7) // 30.14 - 1)
            if width-180 < clickX < width and 10 < clickY < 60:
                playing = False
            print(game.fullColumn(case))
            if not game.fullGrid() and not game.win() and board.inBoard(click) and game.fullColumn(case):
                #caseX = int((clickX % width // 7) // 30.14 - 1)
                game.play(case, 1)
                game.display()
    
    
    
    
    screen.blit(endSurface, endRect)
    pygame.display.flip()
pygame.quit()