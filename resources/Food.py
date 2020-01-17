import pygame
from pygame.locals import *
import random

class Food(pygame.sprite.Sprite):
    def __init__(self,surface):
        super().__init__()
        self.surface = surface
        self.image = pygame.image.load("assets/images/food.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0+self.rect.width/2,320-self.rect.width/2)
        self.rect.centery = 240+self.rect.height/2
        self.move_speed = 1.5
        self.plus_power = True
        self.value = 10

    def update(self):
        self.rect.y = self.rect.y - self.move_speed
        if self.rect.y > 0 - self.rect.height:
            self.surface.blit(self.image,self.rect)
        else:
            pygame.sprite.Sprite.kill(self)
            del self
