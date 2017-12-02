import pygame
import copy as copy
obstacles = []
#the height of the ground
height = 0 


size_h = 64

size_w = 64

screen = pygame.display.set_mode((600,500))


coor = pygame.rect.Rect(300,500-height,64,64)


def getObsticale():

	None


def draw(h,w,image):
	global coor

	for i in range(0,w):
		for j in range(0,h):

			if i<=int(h/2) and j<=int(w/2):
				coord = copy.copy(coor)
				
				coor.x -= i*size_w
				coor.y -= j*size_h
				screen.blit(image[0], coor)
				
				coor = copy.copy(coord)

			elif i<=int(w/2) and j>int(h/2):
				coord = copy.copy(coor)
				
				coor.x -= i*size_w
				coor.y = j*size_h
				screen.blit(image[1], coor)
				
				coor = copy.copy(coord)


			elif i>int(w/2) and j<=int(h/2):
				coord = copy.copy(coor)
				
				coor.x = i*size_w
				coor.y -= j*size_h
				screen.blit(image[2], coor)
				
				coor = copy.copy(coord)



			elif i>int(w/2) and j>int(h/2):
				coord = copy.copy(coor)

				coor.x = i*size_w
				coor.y = j*size_h
				screen.blit(image[3], coor)

				coor = copy.copy(coord)

	pygame.display.flip()


	if coor.x== 0:
		coor.x=500
	coor.move_ip(-1,0)


def initObstacles(h, imageStr=["../octopuss1.png","N.png","facebook.png", "instagram.png"]):
	global height, obstacles, coor
	height = h
	image = []
	for i in imageStr:
		image.append(pygame.image.load(i))




	print len(image)
	while True:
		screen.fill((255,0,0))

		draw(4,4,image)

		pygame.display.update()



initObstacles(200)
