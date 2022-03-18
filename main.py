from variables import *
try:
    import pygame
    from pygame.locals import *
except:
    print("Vous n'avez pas téléchargé le module pygame ! \n Téléchargez le avec la commande ci-contre : pip install pygame")

from Classes.board import Board
from Classes.pawn import Pawn

while playing:
    #screen design
    screen.fill((30,144,255))

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
                    pawns.append(Pawn((col,row), RED, BORDERRED, caseW, caseH))
                    player = 2
                else:
                    pawns.append(Pawn((col,row), YELLOW, BORDERYELLOW, caseW, caseH))
                    player = 1
                
            if not inGame:
                inGame = True
                soundPlayed = False
                game.resetGrid()
                pawns = []

    ########PAWNS########
    #if won -> speed decrease for last pawn
    if inGame:
        speed = 0.05
    else:
        speed = 0.02
    #animation
    for i in pawns:
        
        checkMove = i.animation(screen, speed)
        if checkMove:
            inMove = True
    #preview of play
    if board.inBoard(posMouse) and inGame and col !=7 and col !=-1 and not game.fullColumn(col):
        lastcol = col
        if player == 1:
            board.seePawn(col, (255,50,50))   
        else:
            board.seePawn(col, (255,215,0))
         
    
    ########STATE OF THE GAME########
    status = game.win()
    if game.fullGrid() and not inMove:
        inGame = False
        draw.display()
    elif status and not inMove:
        if not soundPlayed:
            winSound.play()
        if status == 1 and not soundPlayed:
            winRedCTR += 1
            winRed.display()
        elif status == 2 and not soundPlayed:
            winYellowCTR += 1
            winYellow.display()
        inGame = False
        soundPlayed = True
        status = 0  
    elif status:
        if status == 1 and inGame:
            winRedCTR += 1
        elif status == 2 and inGame:
            winYellowCTR += 1
        inGame = False
        
    

    ########TEXTS########
    if player == 1 and inGame:
        redTurn.display()
    elif player == 2 and inGame:
        yellowTurn.display()
    if not inGame and not inMove:
        newGame.display()
    elif not game.isEmpty() and inGame:
        screen.blit(cancelSurface, cancelRect)
    #counters
    yellowCounterSurface = littleFont.render("yellow : {0}".format(winYellowCTR), True, (255,255,0))
    redCounterSurface = littleFont.render("red       : {0}".format(winRedCTR), True, (255,0,0))

    ########BLITS########
    screen.blit(yellowCounterSurface, yellowCounterRect)
    screen.blit(redCounterSurface, redCounterRect)
    screen.blit(endSurface, endRect)

    inMove = False
    pygame.display.flip()
pygame.quit()