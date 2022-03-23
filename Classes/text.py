"""init a text"""
import variables as var
class Text:
    """init a text"""
    def __init__(self,text, font, pos, color):
        self.screen = var.screen
        self.text = text
        self.font = font
        self.color = color
        self.pos = pos
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect(midbottom=self.pos)

    def display(self):
        """displaying the text"""
        self.screen.blit(self.surface,self.rect)

    def get_text(self):
        """return the text of the text"""
        return self.text
