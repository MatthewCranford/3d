import pygame
import time
import random

try:
	import pygame._view
except:
	pass

pygame.init()

fps = 30
clock = pygame.time.Clock()

display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('3d')

white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
light_red = (255,0,0)
yellow = (200,200,0)
light_yellow =(255,255,0)
green = (34,177,76)
light_green = (0,255,0)

small_font = pygame.font.SysFont("comicsansms",25)    
med_font = pygame.font.SysFont("comicsansms",50) 
large_font = pygame.font.SysFont("comicsansms",80)

def cube(start_point, full_size):

	offset = int(full_size / 2)
	x_mid = int(display_width / 2)
	x_offset = int(start_point[0]-x_mid)
	y_mid = int(display_height / 2)
	y_offset = int(start_point[1]-y_mid)
	
	if x_offset < -100:
		x_offset = -100
	elif x_offset > 100:
		x_offset = 100
	
	node_1 = [start_point[0], start_point[1]]
	node_2 = [start_point[0]+full_size, start_point[1]]
	node_3 = [start_point[0], start_point[1]+full_size]
	node_4 = [start_point[0]+full_size, start_point[1]+full_size]

	node_5 = [node_1[0]+x_offset, node_1[1]-y_offset]
	node_6 = [node_2[0]+x_offset, node_2[1]-y_offset]
	node_7 = [node_3[0]+x_offset, node_3[1]-y_offset]
	node_8 = [node_4[0]+x_offset, node_4[1]-y_offset]

	# top line
	pygame.draw.line(game_display, white, (node_1), (node_2))
	# bottom line
	pygame.draw.line(game_display, white, (node_3), (node_4))
	# left line
	pygame.draw.line(game_display, white, (node_1), (node_3))
	# right line
	pygame.draw.line(game_display, white, (node_2), (node_4))

	# top line
	pygame.draw.line(game_display, white, (node_5), (node_6))
	# bottom line
	pygame.draw.line(game_display, white, (node_7), (node_8))
	# left line
	pygame.draw.line(game_display, white, (node_5), (node_7))
	# right line
	pygame.draw.line(game_display, white, (node_6), (node_8))

	pygame.draw.circle(game_display, light_green, node_1, 5)
	pygame.draw.circle(game_display, light_green, node_2, 5)
	pygame.draw.circle(game_display, light_green, node_3, 5)
	pygame.draw.circle(game_display, light_green, node_4, 5)

	pygame.draw.circle(game_display, light_green, node_5, 5)
	pygame.draw.circle(game_display, light_green, node_6, 5)
	pygame.draw.circle(game_display, light_green, node_7, 5)
	pygame.draw.circle(game_display, light_green, node_8, 5)


	pygame.draw.line(game_display, white, (node_1), (node_5))
	pygame.draw.line(game_display, white, (node_2), (node_6))
	pygame.draw.line(game_display, white, (node_3), (node_7))
	pygame.draw.line(game_display, white, (node_4), (node_8))


def game_loop():

	location = [400,300]
	size = 300
	x_move = 0
	y_move = 0
	z_move = 0 
	z_location = 50
	
	while True:	

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_move = -5
				elif event.key == pygame.K_RIGHT:
					x_move = 5
				elif event.key == pygame.K_UP:
					y_move = -5
				elif event.key == pygame.K_DOWN:
					y_move = 5		

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT and x_move == -5 or \
							event.key == pygame.K_RIGHT and x_move == 5:
					x_move = 0
				if event.key == pygame.K_UP and y_move == -5 or \
							event.key == pygame.K_DOWN and y_move == 5:
					y_move = 0
					#x_move = 0
		
		
		
		game_display.fill(black)

		

		if z_location > 200:
			z_move = 0
		z_location += z_move
		#print(z_location)

		current_size = int(size / (z_location*0.1))

		#current_size = size + z_location 
		# if current_size <= 0: 
		# 	current_size = 0 
		# 	z_location = 0 
		# 	x_move = 0
		# 	size = 0            

		location[0] += x_move
		location[1] += y_move

		cube(location, current_size)
		pygame.display.update()
		
		clock.tick(fps)

	pygame.quit()
	quit()

game_loop()