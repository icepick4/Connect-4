"""main"""
from variables import (
                        width,
                        case_w,
                        case_h,
                        screen,
                        end_rect,
                        cancel_rect,
                        game,
                        font,
                        little_font,
                        RED,
                        YELLOW,
                        BLACK,
                        WINREDCTR,
                        WINYELLOWCTR,
                        PLAYING,
                        PLAYER,
                        INGAME,
                        INMOVE,
                        win_red,
                        win_sound,
                        win_yellow,
                        red_turn,
                        yellow_turn,
                        new_game,
                        draw,
                        yellow_counter_rect,
                        red_counter_rect,
                        height,
                        AI,
                        AI_text,
                        AI_turn
)
try:
    import pygame
except ModuleNotFoundError:
    print("""Vous n'avez pas téléchargé le module pygame !
    \n Téléchargez le avec la commande ci-contre : pip install pygame""")

from board import Board
from pawn import Pawn
from check_box import CheckBox
def in_board(click):
    """check if the mouse is in board"""
    #check pos mouse in board
    return case_w <= click[0] < case_w * 8 and case_h <= click[1] < case_h * 7
pawns = []
check_box = CheckBox(screen, (10, height / 9), 170,47)
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
    if cancel_rect.left < pos_x < cancel_rect.right and cancel_rect.top <pos_y< cancel_rect.bottom:
        cancel_surface = little_font.render("CANCEL LAST MOVE", True, (200,185,10))
    else:
        cancel_surface = little_font.render("CANCEL LAST MOVE", True, (0,0,0))
    for event in pygame.event.get():
        if event.type == 256:
            PLAYING = False
        elif event.type == 1025 and event.button == 1 and in_board((pos_x, pos_y)):
            #on presse une colonne
            check_full_col = not game.full_column(col)
            if check_full_col and INGAME and col !=7 and col !=-1:
                INGAME = True
                if PLAYER == 1:
                    row = game.play(col, PLAYER)
                    pawns.append(Pawn((col,row), RED,case_w, case_h))
                    PLAYER = 2
                elif PLAYER == 2 and not AI:
                    row = game.play(col, PLAYER)
                    pawns.append(Pawn((col,row), YELLOW,case_w, case_h))
                    PLAYER = 1
            if not INGAME:
                INGAME = True
                SOUND_PLAYED = False
                game.reset_grid()
                pawns = []
        elif event.type == 1025 and event.button == 1:
            if check_box.check_mouse((pos_x, pos_y)) and not INGAME:
                AI = not AI
                PLAYER = 1
                if AI:
                    AI_text.surface = AI_text.font.render("AI ON", True, BLACK)
                else:
                    AI_text.surface = AI_text.font.render("AI OFF", True, BLACK)
            #on presse le bouton close
            if end_rect.left < pos_x < end_rect.right and end_rect.top < pos_y < end_rect.bottom:
                PLAYING = False
            width_cancel = cancel_rect.left<pos_x<cancel_rect.right
            height_cancel = cancel_rect.top<pos_y<cancel_rect.bottom
            #on presse le bouton cancel
            if width_cancel and height_cancel and not game.is_empty() and not AI:
                game.remove_last_pawn()
                pawns.pop()
                if PLAYER == 1:
                    PLAYER = 2
                else:
                    PLAYER = 1

    #if won -> SPEED decrease for last pawn
    if INGAME:
        SPEED = 0.05
    else:
        SPEED = 0.02
    #animation
    for i in pawns:
        checkMove = i.animation(screen, SPEED)
        if checkMove:
            INMOVE = True
    if PLAYER == 2 and not INMOVE and AI and INGAME:
        INMOVE = True
        best_move = game.play_ai(2)
        row = game.play(best_move, PLAYER)
        pawns.append(Pawn((best_move,row), YELLOW,case_w, case_h))
        PLAYER = 1
    ########PAWNS########
    #preview of play
    if in_board((pos_x, pos_y)) and INGAME and col !=7 and col !=-1 and not game.full_column(col):
        lastcol = col
        if PLAYER == 1:
            board.see_pawn(col, (255,50,50))
        elif PLAYER == 2 and not AI:
            board.see_pawn(col, (255,215,0))
    ########STATE OF THE GAME########
    STATUS = game.win()
    if STATUS and not INMOVE:
        if not SOUND_PLAYED:
            win_sound.play()
        if STATUS == 1 and not SOUND_PLAYED:
            WINREDCTR += 1
            if AI:
                PLAYER = 1
        elif STATUS == 1:
            win_red.display(screen)
        if STATUS == 2 and not SOUND_PLAYED:
            WINYELLOWCTR += 1
        elif STATUS == 2:
            win_yellow.display(screen)
        INGAME = False
        SOUND_PLAYED = True
        STATUS = 0
    elif STATUS:
        INGAME = False
    elif game.full_grid() and not INMOVE:
        INGAME = False
        draw.display(screen)
    ########TEXTS########
    if PLAYER == 1 and INGAME:
        red_turn.display(screen)
    elif PLAYER == 2 and INGAME and not AI:
        yellow_turn.display(screen)
    elif PLAYER == 2 and INGAME and AI:
        AI_turn.display(screen)
    if not INGAME and not INMOVE:
        AI_text.display(screen)
        new_game.display(screen)
    elif not game.is_empty() and INGAME and not AI:
        screen.blit(cancel_surface, cancel_rect)
    #counters
    yellowCounterSurface = little_font.render(f"yellow : {WINYELLOWCTR}", True, (255,255,0))
    redCounterSurface = little_font.render(f"red       : {WINREDCTR}", True, (255,0,0))

    ########BLITS########
    screen.blit(yellowCounterSurface, yellow_counter_rect)
    screen.blit(redCounterSurface, red_counter_rect)
    screen.blit(end_surface, end_rect)

    INMOVE = False
    pygame.display.flip()
pygame.display.quit()
