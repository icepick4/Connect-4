"""class for the checkbox"""
from tkinter.tix import Tree
import pygame

class CheckBox:
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
        return self.checked

    def check_mouse(self, mouse_pos):
        if self.pos[0] < mouse_pos[0] < self.pos[0] + self.width and self.pos[1] < mouse_pos[1] < self.pos[1] + self.height:
            self.checked = not self.checked
            return True
        return False