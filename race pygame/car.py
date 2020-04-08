import pygame
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (20, 255, 140)
GREY = (210, 210 ,210)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
 

class Car (pygame.sprite.Sprite):
	
	def __init__(self, filename, colorkey, posX = 0, posY = 0):
		super().__init__()
		self.image = pygame.image.load(filename)
		self.image.set_colorkey(colorkey)
		self.rect = self.image.get_rect()
		self.rect.x = posX
		self.rect.y = posY
		self.angle = 0
		self.angle_change = 0

		if self.rect.collidepoint(1000,1000):
			pygame.quit()
		
	def update(self,tap):
		if tap[pygame.K_UP]:
			self.rect.x += 1
		if tap[pygame.K_DOWN]:
 			self.rect.x -= 1

 		# boundaries to keep player in the game window
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > SCREEN_WIDTH:
			self.rect.right = SCREEN_WIDTH
		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= SCREEN_HEIGHT:
			self.rect.bottom = SCREEN_HEIGHT