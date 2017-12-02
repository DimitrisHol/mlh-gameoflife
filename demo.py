import pygame

obstacles = []
#the height of the ground
height = 0 

screen = pygame.display.set_mode((600,500))




def getObsticale():

	None


def draw():
	None


def initObstacles(h, image=["octopuss1.png","N.png","facebook.png", "instagram.png"]):
	global height, obstacles
	height = h

	for i in image:
		image = pygame.image.load(i)


	obstacles.append(pygame.rect.Rect(300,500-height,64,64))
	print obstacles[0]
	obstacles[0].move_ip(-3,0)
	print obstacles[0]



	print height
	while True:
		screen.fill((255,0,0))
		if obstacles[0].x== 0:
			obstacles[0].x=500
		obstacles[0].move_ip(-1,0)
		screen.blit(image, obstacles[0])

		pygame.display.flip()

		pygame.display.update()



initObstacles(25)
