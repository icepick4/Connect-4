from variables import *
try:
    import pygame
    from pygame.locals import *
except:
    print("Vous n'avez pas téléchargé le module pygame ! \n Téléchargez le avec la commande ci-contre : pip install pygame")

from Classes.board import Board
while playing:
    screen.fill((30,144,255))
    pygame.draw.rect(screen, (45,45,45), (0,height - height // 8, width, height))
    board = Board(width, height, screen)
    posMouse = pygame.mouse.get_pos()
    posX = posMouse[0]
    posY = posMouse[1]
    case = int((posX % width // 7) // (width / 7 % width / 9) - 1)
    if endRect.left < posX < endRect.right and endRect.top < posY < endRect.bottom:
        endSurface = font.render("CLOSE", True, (255,60,60))
    else:
        endSurface = font.render("CLOSE", True, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            #on presse le bouton close
            if endRect.left < posX < endRect.right and endRect.top < posY < endRect.bottom:
                playing = False
            if board.inBoard(posMouse) and not game.fullColumn(case) and inGame and case !=7 and case !=-1:
                inGame = True
                game.play(case, player)       
                if player == 1:
                    player = 2
                else:
                    player = 1
            if not inGame:
                inGame = True
                game.resetGrid()
    board.drawPawn(game)
    if board.inBoard(posMouse) and inGame and case !=7 and case !=-1 and not game.fullColumn(case):
        if player == 1:
            board.seePawn(case, game, (255,50,50))   
        else:
            board.seePawn(case, game, (255,215,0))  
    status = game.win()
    if game.fullGrid():
        inGame = False
        draw.display()
    elif status:
        if status == 1:
            if inGame:
                winRedCTR += 1
            winRed.display()
        elif status == 2:
            if inGame:
                winYellowCTR +=1
            winYellow.display()
        inGame = False
        status = 0
    if player == 1 and inGame:
        redTurn.display()
    elif player == 2 and inGame:
        yellowTurn.display()
    if not inGame:
        newGame.display()

    
    yellowCounterSurface = font.render("yellow : {0}".format(winYellowCTR), True, (255,255,0))
    redCounterSurface = font.render("red       : {0}".format(winRedCTR), True, (255,0,0))
    screen.blit(yellowCounterSurface, yellowCounterRect)
    screen.blit(redCounterSurface, redCounterRect)
    screen.blit(endSurface, endRect)
    pygame.display.flip()
pygame.quit()