"""imports"""
import pygame
from variables import RED, BORDERRED, BORDERYELLOW, BLACK, GREY, case_w, case_h

class Board:
    """setting the board"""
    def __init__(self,screen):
        self.screen = screen
        self.draw_board()
        pygame.draw.line(
                        self.screen,
                        BLACK,
                        (0,case_h * 8 - 2),
                        (case_w * 9 + 20,case_h * 8 - 2),
                        12
                    )

    def draw_board(self):
        """drawing the board"""
        #vertical
        for i in range(8):
            pygame.draw.line(
                            self.screen,
                            BLACK,
                            (case_w + i * case_w + 2, case_h *2),
                            (case_w + i * case_w + 2, case_h * 8),
                            2
                        )
            pygame.draw.line(
                            self.screen,
                            GREY,
                            (case_w + i * case_w, case_h*2),
                            (case_w + i * case_w, case_h * 8),
                            4
                        )
            pygame.draw.line(
                            self.screen,
                            BLACK,
                            (case_w + i * case_w - 2, case_h*2),
                            (case_w + i * case_w - 2, case_h * 8),
                            2
                        )
        #horizontal
        for i in range(7):
            pygame.draw.line(
                            self.screen,
                            BLACK,
                            (case_w, case_h *2 + i * case_h + 2),
                            (case_w * 9 - case_w, case_h *2 + i * case_h + 2),
                            2
                        )
            pygame.draw.line(
                            self.screen,
                            GREY,
                            (case_w, case_h *2+ i * case_h),
                            (case_w * 9 - case_w, case_h *2 + i * case_h),
                            4
                        )
            pygame.draw.line(
                            self.screen,
                            BLACK,
                            (case_w, case_h *2 + i * case_h - 2),
                            (case_w * 9 - case_w, case_h *2 + i * case_h - 2),
                            2
                        )

    def see_pawn(self, col, color):
        """preview the pawns"""
        if color == RED:
            border_color = BORDERRED
        else:
            border_color = BORDERYELLOW
        pygame.draw.circle(
                            self.screen,
                            border_color,
                            (case_w + col * case_w + case_w /2,case_h*2 + -1 * case_h + case_h /2),
                            (case_w / 4) + 5,
                            5
                    )
        pygame.draw.circle(
                            self.screen,
                            color,
                            (case_w + col * case_w + case_w /2,case_h*2 + -1 * case_h + case_h /2),
                            case_w / 4
                    )
