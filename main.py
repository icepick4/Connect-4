from variables import *
try:
    import pygame
except:
    print("Vous n'avez pas téléchargé le module pygame ! \n Téléchargez le avec la commande ci-contre : pip install pygame")

from Classes.board import Board
from Classes.pawn import Pawn

def in_board(click):
    """check if the mouse is in board"""
    #check pos mouse in board
    return case_w <= click[0] < case_w * 8 and case_h <= click[1] < case_h * 7
while PLAYING:
    #screen design
    screen.fill((30,144,255))

    board = Board(screen)

    #pos mouse
    pos_x, pos_y = pygame.mouse.get_pos()

    #current column
    col = int((pos_x % width // 7) // (width / 7 % width / 9) - 1)

    #hover effects
    if end_rect.left < pos_x < end_rect.right and end_rect.top < pos_y < end_rect.bottom:
        end_surface = font.render("CLOSE", True, (255,60,60))
    else:
        end_surface = font.render("CLOSE", True, (0,0,0))
    if cancel_rect.left < pos_x < cancel_rect.right and cancel_rect.top < pos_y < cancel_rect.bottom:
        cancel_surface = little_font.render("CANCEL LAST MOVE", True, (200,185,10))
    else:
        cancel_surface = little_font.render("CANCEL LAST MOVE", True, (0,0,0))

    for event in pygame.event.get():
        if event.type == 256:
            PLAYING = False
        elif event.type == 1025 and event.button == 1 :
            #on presse le bouton close
            if end_rect.left < pos_x < end_rect.right and end_rect.top < pos_y < end_rect.bottom:
                PLAYING = False
            #on presse le bouton cancel
            elif cancel_rect.left < pos_x < cancel_rect.right and cancel_rect.top < pos_y < cancel_rect.bottom and not game.is_empty():
                game.remove_last_pawn()
                pawns.pop()
                if PLAYER == 1:
                    PLAYER = 2
                else:
                    PLAYER = 1
            #on presse une colonne
            if in_board((pos_x, pos_y)) and not game.full_column(col) and INGAME and col !=7 and col !=-1:
                INGAME = True
                row = game.play(col, PLAYER)       
                if PLAYER == 1:
                    pawns.append(Pawn((col,row), RED,case_w, case_h))
                    PLAYER = 2
                else:
                    pawns.append(Pawn((col,row), YELLOW,case_w, case_h))
                    PLAYER = 1
                
            if not INGAME:
                INGAME = True
                soundPlayed = False
                game.reset_grid()
                pawns = []

    ########PAWNS########
    #if won -> speed decrease for last pawn
    if INGAME:
        speed = 0.05
    else:
        speed = 0.02
    #animation
    for i in pawns:
        
        checkMove = i.animation(screen, speed)
        if checkMove:
            INMOVE = True
    #preview of play
    if in_board((pos_x, pos_y)) and INGAME and col !=7 and col !=-1 and not game.full_column(col):
        lastcol = col
        if PLAYER == 1:
            board.see_pawn(col, (255,50,50))   
        else:
            board.see_pawn(col, (255,215,0))
         
    
    ########STATE OF THE GAME########
    status = game.win()
    if status and not INMOVE:
        if not soundPlayed:
            win_sound.play()
        if status == 1 and not soundPlayed:
            WINREDCTR += 1
        elif status == 1:
            win_red.display()
        if status == 2 and not soundPlayed:
            WINYELLOWCTR += 1
        elif status == 2:
            win_yellow.display()
        INGAME = False
        soundPlayed = True
        status = 0  
    elif status:
        INGAME = False
    elif game.full_grid() and not INMOVE:
        INGAME = False
        draw.display()
        
    

    ########TEXTS########
    if PLAYER == 1 and INGAME:
        red_turn.display()
    elif PLAYER == 2 and INGAME:
        yellow_turn.display()
    if not INGAME and not INMOVE:
        new_game.display()
    elif not game.is_empty() and INGAME:
        screen.blit(cancel_surface, cancel_rect)
    #counters
    yellowCounterSurface = little_font.render("yellow : {0}".format(WINYELLOWCTR), True, (255,255,0))
    redCounterSurface = little_font.render("red       : {0}".format(WINREDCTR), True, (255,0,0))

    ########BLITS########
    screen.blit(yellowCounterSurface, yellow_counter_rect)
    screen.blit(redCounterSurface, red_counter_rect)
    screen.blit(end_surface, end_rect)

    INMOVE = False
    pygame.display.flip()
pygame.display.quit()