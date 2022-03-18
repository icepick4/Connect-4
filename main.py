from variables import *
try:
    import pygame
    from pygame.locals import *
except:
    print("Vous n'avez pas téléchargé le module pygame ! \n Téléchargez le avec la commande ci-contre : pip install pygame")

from Classes.board import Board
from Classes.pawn import Pawn
pawns = []
while playing:
    #screen design
    screen.fill((30,144,255))
    
    #pygame.draw.rect(screen, (45,45,45), (0,height - height // 15, width, height))

    board = Board(width, height, screen)

    #pos mouse
    posMouse = pygame.mouse.get_pos()
    posX = posMouse[0]
    posY = posMouse[1]

    #current column
    col = int((posX % width // 7) // (width / 7 % width / 9) - 1)

    #hover effects
    if endRect.left < posX < endRect.right and endRect.top < posY < endRect.bottom:
        endSurface = font.render("CLOSE", True, (255,60,60))
    else:
        endSurface = font.render("CLOSE", True, (0,0,0))
    if cancelRect.left < posX < cancelRect.right and cancelRect.top < posY < cancelRect.bottom:
        cancelSurface = littleFont.render("CANCEL LAST MOVE", True, (200,185,10))
    else:
        cancelSurface = littleFont.render("CANCEL LAST MOVE", True, (0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            #on presse le bouton close
            if endRect.left < posX < endRect.right and endRect.top < posY < endRect.bottom:
                playing = False
            #on presse le bouton cancel
            elif cancelRect.left < posX < cancelRect.right and cancelRect.top < posY < cancelRect.bottom and not game.isEmpty():
                game.removeLastPawn()
                pawns.pop()
                if player == 1:
                    player = 2
                else:
                    player = 1
            #on presse une colonne
            if board.inBoard(posMouse) and not game.fullColumn(col) and inGame and col !=7 and col !=-1:
                inGame = True
                row = game.play(col, player)       
                if player == 1:
                    pawns.append(Pawn((col,row), RED, BORDERRED, width / 9, height / 8))
                    player = 2
                else:
                    pawns.append(Pawn((col,row), YELLOW, BORDERYELLOW, width / 9, height / 8))
                    player = 1
                
            if not inGame:
                inGame = True
                game.resetGrid()
                pawns = []

    #animate pawns
    for i in pawns:
        checkMove = i.animation(screen)
        if checkMove:
            inMove = True

    #preview of play
    if board.inBoard(posMouse) and inGame and col !=7 and col !=-1 and not game.fullColumn(col):
        lastcol = col
        if player == 1:
            board.seePawn(col, (255,50,50))   
        else:
            board.seePawn(col, (255,215,0))
         

    #state of the game
    status = game.win()
    if game.fullGrid() and not inMove:
        inGame = False
        draw.display()
        
    elif status and inMove:
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

    #texts on top
    if player == 1 and inGame:
        redTurn.display()
    elif player == 2 and inGame:
        yellowTurn.display()
    if not inGame:
        newGame.display()
    elif not game.isEmpty():
        screen.blit(cancelSurface, cancelRect)

    #counters en blits
    yellowCounterSurface = littleFont.render("yellow : {0}".format(winYellowCTR), True, (255,255,0))
    redCounterSurface = littleFont.render("red       : {0}".format(winRedCTR), True, (255,0,0))

    screen.blit(yellowCounterSurface, yellowCounterRect)
    screen.blit(redCounterSurface, redCounterRect)
    screen.blit(endSurface, endRect)

    pygame.display.flip()
pygame.quit()