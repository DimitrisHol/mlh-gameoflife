import pygame
import copy as copy
import sys
from pygame.locals import *
from time import sleep

obstacles = []
#the height of the ground
height = 600 

wight = 900

size_h = 49

size_w = 49

screen = pygame.display.set_mode((wight,height))


coor = pygame.rect.Rect(300,300,20,20)


def getObsticale():

	None


def drawObstacle(h,w,image):
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
		coor.x=wight+100
	coor.move_ip(-5,0)


def initObstacles(h, imageStr=["octopuss1.png","N.png","facebook.png", "instagram.png"]):
	global  obstacles, coor
	coor = pygame.rect.Rect(wight,400,20,20)
	player_coord = pygame.rect.Rect(80,height-h-size_h/2,20,20)

	image = []
	for i in imageStr:
		image.append(pygame.image.load(i))
	hero = pygame.image.load("octopuss1.png")

	for i in image:
		 i = pygame.transform.scale(i, (size_w, size_h))
	image[2] = pygame.transform.rotate(image[2],90)


	print len(image)
	pygame.init()
	while True:
		pygame.time.Clock().tick(60)
		screen.fill((87, 166, 250))
		pygame.draw.rect(screen,(4, 62, 5),(0,height-h-5+size_w/2,wight,height))
		if(player_coord.y<height-h-size_h/2):
			player_coord.y +=7

		screen.blit(hero, player_coord)
		drawObstacle(4,4,image)



		for event in pygame.event.get():
			print pygame.key.get_pressed().index(1)
			if pygame.key.get_pressed().index(1)==27:

				pygame.quit()
				sys.exit()


			elif pygame.key.get_pressed().index(1)==273 or pygame.key.get_pressed().index(1)==119:
				player_coord.y -=size_h*2
				
				print "up"
			elif pygame.key.get_pressed().index(1)==274 or pygame.key.get_pressed().index(1)==115:
				#player_coord.y +=size_h
				print "down"
		#sleep(0.003)




initObstacles(100)
