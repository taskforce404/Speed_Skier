import pygame
import sys
sys.path.append("")
from pygame.locals import *
from tools import creat_font

class Distance():
    def __init__(self,surface):
        self.surface = surface
        self.text = creat_font(size=12).render("距离",True,(150,150,150))
        self.text_rect = self.text.get_rect()
        self.text_rect.x = 5
        self.text_rect.y = 20

        self.distance = 0
        self.distance_text = creat_font(size=12).render(str(self.distance),True,(150,150,150))
        self.distance_text_rect = self.distance_text.get_rect()
        self.distance_text_rect.x = 35
        self.distance_text_rect.y = 21

    def add_distance(self):
        self.distance = self.distance + 1
        self.distance_text = creat_font(size=12).render(str(self.distance),True,(150,150,150))
        self.distance_text_rect = self.distance_text.get_rect()
        self.distance_text_rect.x = 35
        self.distance_text_rect.y = 21

    def blitme(self):
        self.surface.blit(self.text,self.text_rect)
        self.surface.blit(self.distance_text,self.distance_text_rect)