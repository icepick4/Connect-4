from variables import *
try:
    import pygame
    from pygame.locals import *
except:
    print("Vous n'avez pas téléchargé le module pygame ! \n Téléchargez le avec la commande ci-contre : pip install pygame")
from Classes.board import Board
from random import randint

while playing:
    screen.fill((30,144,255))
    board = Board(width, height, screen)
    posMouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            click = event.pos
            clickX = click[0]
            clickY = click[1]
            case = int((clickX % width // 7) // (width/7 % width / 9) - 1)
            #on presse le bouton close
            if width-180 < clickX < width and 10 < clickY < 60:
                playing = False
            if board.inBoard(click) and not game.fullColumn(case) and inGame:
                inGame = True
                #caseX = int((clickX % width // 7) // 30.14 - 1)
                game.play(case, player)
                if player == 1:
                    player = 2
                else:
                    player = 1
            if not inGame:
                inGame = True
                game.resetGrid()
    if board.inBoard(posMouse) and inGame:
        posX = event.pos[0]
        case = int((posX % width // 7) // (width/7 % width / 9) - 1)
        if player == 1:
            board.seePawn(case, game, (255,60,60,128))   
        else:
            board.seePawn(case, game, (255,215,0,128))  
            
    board.drawPawn(game)
    status = game.win()
    if game.fullGrid() or status:
        #print quel joueur à gagné
        inGame = False
        if status == 1:
            winRed.display()
        elif status == 2:
            winYellow.display()
        status = 0
        
    if player == 1 and inGame:
        redTurn.display()
    elif player == 2 and inGame:
        yellowTurn.display()
    if not inGame:
        newGame.display()
    screen.blit(endSurface, endRect)
    pygame.display.flip()
pygame.quit()