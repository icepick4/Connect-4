"""imports"""
import pygame
from game import Game
from text import Text

pygame.display.init()

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
case_w = width / 9
case_h = height / 8
FONTPATH = "assets/font/leaguespartan-bold.ttf"
pygame.font.init()
font = pygame.font.Font(FONTPATH, 50)
little_font = pygame.font.Font(FONTPATH, 43)

PLAYING = True
PLAYER = 1
WINREDCTR = 0
WINYELLOWCTR = 0
IA = False
INGAME = False
INMOVE = False
centered_pos = (width/2, height /13)
red_turn = Text("Red's turn !", font, centered_pos, RED)
yellow_turn = Text("Yellow's turn !", font, centered_pos, YELLOW)
ia_turn = Text("IA's turn !", font, centered_pos, BLACK)
win_red = Text("Red won !", font, centered_pos, RED)
win_yellow = Text("Yellow won !", font, centered_pos, YELLOW)
draw = Text("Draw !", font, centered_pos, BLACK)
new_game = Text("""Click anywhere to start a new game !
                        """,
                        little_font, (width/1.7, height / 8), BLACK)
ia_text = Text("IA OFF", font, (100, height / 6), BLACK)
yellow_counter_surface = little_font.render(f"yellow : {WINYELLOWCTR}", True, (255,255,0))
yellow_counter_rect = yellow_counter_surface.get_rect(topleft = (5,5))
red_counter_surface = little_font.render(f"red       : {WINREDCTR}", True, (255,0,0))
red_counter_rect = red_counter_surface.get_rect(topleft = (5,yellow_counter_rect.bottom))

cancel_surface = little_font.render("CANCEL LAST MOVE", True, (0,0,0))
cancel_rect = cancel_surface.get_rect(midbottom = (width / 2, height / 8))

#bouton pour fermer la fenetre
end_surface = font.render("CLOSE", True, (0,0,0))
end_rect = end_surface.get_rect(topright=(width - 10,10))

#win sound
pygame.mixer.init()
win_sound = pygame.mixer.Sound('assets/audio/win.wav')
game = Game()
pawns = []
