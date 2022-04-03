"""class for the checkbox"""
import pygame

class CheckBox:
    """init the checkbox"""
    def __init__(self, screen, pos, width, height):
        self.color = (0,0,0)
        self.width = width
        self.height = height
        self.screen = screen
        self.pos = pos
        #draw a rectangle with a border of 5px and a color of the checkbox
        self.surface = pygame.Surface(pos, 65536, 32)
        self.checked = False
    def is_checked(self):
        """return if the checkbox is checked"""
        return self.checked

    def check_mouse(self, mouse_pos):
        """check if the mouse is in the checkbox"""
        check_width = self.pos[0] < mouse_pos[0] < self.pos[0] + self.width
        check_height = self.pos[1] < mouse_pos[1] < self.pos[1] + self.height
        if check_width and check_height:
            self.checked = not self.checked
            return True
        return False
