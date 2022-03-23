"""imports"""
import pygame
from variables import case_w, case_h

class Pawn:
    """init a pawn on the screen"""
    def __init__(self, pos, color, width, height):
        self.last_row = pos[1]
        self.col = pos[0]
        self.row_animation = -1
        self.color = color
        if color == (255,50,50):
            border_color = (200,0,0)
        else:
            border_color = (160,150,5)
        self.surface = pygame.Surface((case_w, case_h), 65536, 32)
        self.surface = self.surface.convert_alpha()

        pygame.draw.circle(self.surface, color, (width / 2,height / 2), case_w / 4)
        pygame.draw.circle(self.surface, border_color, (width / 2,height / 2), (case_w / 4) + 5, 5)

    def animation(self, screen, speed):
        """animate the current pawn"""
        #new pos
        rect = self.surface.get_rect(
                                midtop = (
                                    case_w + self.col * case_w + case_w /2,
                                    case_h*2 + self.row_animation * case_h - self.row_animation * 1
                                    )
                                )
        #while new row not reached -> row grows
        if self.row_animation < self.last_row:
            self.row_animation += speed
            in_move = True
        else:
            in_move = False
        screen.blit(self.surface, rect)
        #return the state to let the pawns move while the game's won
        return in_move

    def get_color(self):
        """return the color of the current pawn"""
        return self.color
