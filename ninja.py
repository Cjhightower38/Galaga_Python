import pygame

class Ninja():
	
	def __init__(self, screen):
		self.screen = screen
		
		self.image = pygame.image.load('images/ninja.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)
