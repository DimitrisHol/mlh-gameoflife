import pygame
import copy as copy
import sys
<<<<<<< HEAD
from pygame.locals import *
=======
>>>>>>> ae75029e9e056155d6296f1a74326d5d2cb5986e
obstacles = []
#the height of the ground
height = 600 

wight = 600

size_h = 49

size_w = 49

screen = pygame.display.set_mode((height,wight))


coor = pygame.rect.Rect(300,300,20,20)


def getObsticale():

    None


def draw(h,w,image):
    global coor

<<<<<<< HEAD
	for i in range(0,w):
		for j in range(0,h):
			coord = pygame.rect.Rect(300,300,10,10)

			if i<int(w/2) and j<int(h/2):

				
				coord.x = coor.x - (i)*(size_w/2)
				coord.y = coor.y - (j)*(size_h/2)
				screen.blit(image[0], coord)
				

			elif i<int(w/2) and j>=int(h/2):
				
				coord.x = coor.x - (i)*(size_w/2)
				coord.y = coor.y + (j)*(size_h/2)
				screen.blit(image[1], coord)
				

			elif i>=int(w/2) and j<int(h/2):
				
				coord.x = coor.x + (i)*(size_w/2)
				coord.y = coor.y - (j)*(size_h/2)
				screen.blit(image[2], coord)
			

			elif i>=int(w/2) and j>=int(h/2):

				coord.x = coor.x + (i)*(size_w/2)
				coord.y = coor.y + (j)*(size_h/2)
				screen.blit(image[3], coord)

=======
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
>>>>>>> ae75029e9e056155d6296f1a74326d5d2cb5986e

                coor = copy.copy(coord)


<<<<<<< HEAD
	if coor.x== -500:
		coor.x=700
	coor.move_ip(-1,0)
=======
>>>>>>> ae75029e9e056155d6296f1a74326d5d2cb5986e

            elif i>int(w/2) and j>int(h/2):
                coord = copy.copy(coor)

<<<<<<< HEAD
def initObstacles(h, imageStr=["../octopuss1.png","N.png","facebook.png", "instagram.png"]):
	global  obstacles, coor
	image = []
	for i in imageStr:
		image.append(pygame.image.load(i))

#	for i in image:
#		picture = pygame.transform.scale(i,(size_w,size_h))


	print len(image)
	pygame.init()
	while True:
		screen.fill((87, 166, 250))
		pygame.draw.rect(screen,(4, 62, 5),(0,height-h-5+size_w/2,wight,height))
=======
                coor.x = i*size_w
                coor.y = j*size_h
                screen.blit(image[3], coor)

                coor = copy.copy(coord)

    pygame.display.flip()


    if coor.x== 0:
        coor.x=500
    coor.move_ip(-1,0)
>>>>>>> ae75029e9e056155d6296f1a74326d5d2cb5986e


<<<<<<< HEAD
		for event in pygame.event.get():
			if pygame.key.get_pressed().index(1)==27:
	
			#if event.type==pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()



=======
def initObstacles(h, imageStr=["octopuss1.png","N.png","facebook.png", "instagram.png"]):
    global height, obstacles, coor
    height = h
    image = []
    for i in imageStr:
        image.append(pygame.image.load(i))

    print len(image)
    while True:
        screen.fill((255,0,0))

        draw(4,4,image)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.display.update()

def quit():
    pygame.display.quit()
    pygame.quit()
    sys.exit()
>>>>>>> ae75029e9e056155d6296f1a74326d5d2cb5986e



initObstacles(200)
