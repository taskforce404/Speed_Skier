import pygame
from pygame.locals import *

class Beibei(pygame.sprite.Sprite):
	def __init__(self,surface):
		super().__init__()
		self.surface = surface
		self.image = pygame.image.load("assets/images/skiing.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = surface.get_rect().centerx
		#以下为试验
		self.frame = 0
		self.tick_time = 0

	def blitme(self,dt):
		self.tick_time = self.tick_time + dt
		if self.tick_time >= 1000/5:
			self.frame = self.frame + 1
			self.tick_time = 0
			print(self.frame)
		self.surface.blit(self.image,self.rect)