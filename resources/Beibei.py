import pygame
from pygame.locals import *

class Beibei(pygame.sprite.Sprite):
	def __init__(self,surface):
		super().__init__()
		self.surface = surface
		self.image = pygame.image.load("assets/images/skiing.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = surface.get_rect().centerx
		self.movespeed = 2
		self.move_time = 0
		self.frame = 0
		self.tick_time = 0

	def blitme(self,dt):
		self.tick_time = self.tick_time + dt
		if self.tick_time >= 1000/5:
			self.frame = self.frame + 1
			self.tick_time = 0
			# print(self.frame)
		self.surface.blit(self.image,self.rect)

	def increase_movespeed(self,dt):
		if self.movespeed < 4:
			self.move_time = self.move_time + dt
			if self.move_time >= 1000/100:
				self.movespeed = self.movespeed + 0.5
				self.move_time = 0

