import pygame
pygame.init()
screen = pygame.display.set_mode((670, 800))

running = True
y1, y2 = 600, 600
acc1, acc2 = 0.2, 0.1
t_width, t_height = 20, 25
i = 0

def move():
	global y1, y2, acc1, acc2
	if y1 >= 60:
		y1 -= acc1
		acc1 += 0.02
	if y2 >= 60:
		y2 -= acc2
		acc2 += 0.01

while running:
	screen.fill((100, 100, 100))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	#drawing the cars
	pygame.draw.rect(screen, (0, 255, 0), (150, y1, 70, 140))
	pygame.draw.rect(screen, (200, 0, 0), (450, y2, 70, 140))
	
	#drawing the tyres of car 1
	pygame.draw.rect(screen, (0, 0, 0), (150-t_width, y1+140-t_height, t_width, t_height))
	pygame.draw.rect(screen, (0, 0, 0), (150-t_width, y1+10, t_width, t_height))
	pygame.draw.rect(screen, (0, 0, 0), (220, y1+140-t_height, t_width, t_height))
	pygame.draw.rect(screen, (0, 0, 0), (220, y1+10, t_width, t_height))
	
	#drawing the tyres of car 2
	pygame.draw.rect(screen, (0, 0, 0), (450-t_width, y2+140-t_height, t_width, t_height))
	pygame.draw.rect(screen, (0, 0, 0), (450-t_width, y2+10, t_width, t_height))
	pygame.draw.rect(screen, (0, 0, 0), (520, y2+140-t_height, t_width, t_height))
	pygame.draw.rect(screen, (0, 0, 0), (520, y2+10, t_width, t_height))
	
	#start line
	pygame.draw.rect(screen, (140, 140, 140), (0, 770, 670, 30))
	
	#finish line
	pygame.draw.rect(screen, (140, 140, 140), (0, 30, 670, 30))
	if i >= 140:
		move()
		
	i += 1
	
	pygame.display.flip()

pygame.quit()
