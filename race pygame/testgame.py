import pygame
from pygame.locals import *
import random
from car import Car
import time

#initialize game
pygame.init()

width = 900
height= 290
#display width by height
game_display = pygame.display.set_mode((width ,height))

#colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (20, 255, 140)
GREY = (210, 210 ,210)

#game clock
clock = pygame.time.Clock()

spritesALL = pygame.sprite.Group()

playerCar = Car("f1car.png",WHITE)
playerCar.rect.x = 10
playerCar.rect.y = 60
spritesALL.add(playerCar)

road = pygame.image.load("street.png")


def eventGAME():
    for event in pygame.event.get():
        #this lets the user exit the game by clickin X or escape or q to end the game display
        if event.type == QUIT or (event.type == KEYDOWN and (event.type == K_ESCAPE or event.key == K_q)):
            pygame.quit()
            quit()

myfont = pygame.font.SysFont('Comic Sans MS',40)

win = myfont.render("You Win!",1, BLACK)

lose = myfont.render("You Lose!",1,BLACK)

def start():
	intro = True
	large = pygame.font.SysFont('Comic Sans MS',30)
	game = large.render("Drag Race",1,BLACK)
	control = large.render("Use up key to speed up.",1,BLACK)
	winning = large.render("Get to the other end of the window before 20 seconds and you win.",1,BLACK)
	game_display.blit(game,(20,20))
	game_display.blit(control,(10,230))
	game_display.blit(winning,(10,260))
	pygame.display.update()	

def gamePlay():
	running = 1
	exitcode = 0 
	n = 0
	large = pygame.font.SysFont('Comic Sans MS',30)
	
	while running:
		clock.tick(60)
		
		start()
		
		pygame.display.flip()
		
		# ability to exit game
		eventGAME()
		#gameDisplay()
		game_display.fill(WHITE)
				

		rel_x = n % road.get_rect().width
		game_display.blit(road,(rel_x - road.get_rect().width,0))
		if rel_x <= width:
		 	game_display.blit(road,(rel_x,0))
		n -=1
		
	    # enter race car
		spritesALL.draw(game_display)
	
		tap = pygame.key.get_pressed()

		playerCar.update(tap)
		x = playerCar.rect.x

		if x == (width-120)  and pygame.time.get_ticks() >= 0:
			time.sleep(1)
			game_display.blit(win,(100,150))
			
		elif pygame.time.get_ticks() >= 20000:
			time.sleep(1)
			game_display.blit(lose,(100,150))
		pygame.display.flip()
	pygame.quit()
			

if __name__== "__main__":
	gamePlay()
	pygame.quit()
quit()
    