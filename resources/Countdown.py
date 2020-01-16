import pygame
import sys
sys.path.append("")
from pygame.locals import *
from tools import creat_font

class Countdown():
    def __init__(self,surface):
        self.surface = surface
        self.text = ["3","2","1","GO"]
        self.now = 0
        self.font = creat_font(size=50).render(self.text[self.now],True,(150,150,150))
        self.rect = self.font.get_rect()
        self.rect.centerx = self.surface.get_rect().centerx
        self.rect.centery = self.surface.get_rect().centery

    def update_now(self):
        self.now = self.now + 1
        if self.now <= 3:
            self.font = creat_font(size=50).render(self.text[self.now],True,(150,150,150))
            self.rect = self.font.get_rect()
            self.rect.centerx = self.surface.get_rect().centerx
            self.rect.centery = self.surface.get_rect().centery
            
    def blitme(self):
        if self.now <= 3:
            self.surface.blit(self.font,self.rect)


