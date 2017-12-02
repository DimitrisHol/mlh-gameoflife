import pygame
import copy as copy
import sys
from pygame.locals import *
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


	pygame.display.flip()


	if coor.x== -500:
		coor.x=700
	coor.move_ip(-1,0)


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

		draw(4,4,image)

		for event in pygame.event.get():
			if pygame.key.get_pressed().index(1)==27:
	
			#if event.type==pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()






initObstacles(200)
