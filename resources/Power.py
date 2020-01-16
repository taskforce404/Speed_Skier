import pygame
import sys
sys.path.append("")
from pygame.locals import *
from tools import creat_font

class Power():
    def __init__(self,surface):
        self.surface = surface
        self.text = creat_font(size=12).render("体力",True,(150,150,150))
        self.text_rect = self.text.get_rect()
        self.text_rect.x = 5
        self.text_rect.y = 5
        self.power_num = 80

    def blitme(self):
        self.surface.blit(self.text,self.text_rect)
        pygame.draw.line(self.surface,(150,150,150),(35,11),(35+self.power_num,11),10)

    def reduce_power(self,num):
        self.power_num = self.power_num - num

