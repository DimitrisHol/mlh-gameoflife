import pygame
import time
import random

pygame.init()

display_width = 1200
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,200,0)
cyan = (0,255,255)
bright_red = (255,0,0)
bright_green = (0,255,0)
block_color = (53,115,255)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Legend27TheGame')
icon = pygame.image.load('octo.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

backImg = pygame.image.load('background0.png')


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1:
            if action == 2:
                #action()
                print('about')
                about()
            elif action == 1:
                print('play')
            elif action == 3:
                print('settings')

    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont('freesansbold.ttf',50)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def about():
    print('me')

    gameDisplay.fill(white)
    gameDisplay.blit(backImg,(0,0))
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects("me", largeText)
    TextRect.center = ((display_width/2),(display_height/4))
    gameDisplay.blit(TextSurf, TextRect)

about()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        gameDisplay.blit(backImg,(0,0))
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("THE Game", largeText)
        TextRect.center = ((display_width/2),(display_height/4))
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()


        button("Play!",500,250,200,50,green,bright_green,1)
        button("About",500,350,200,50,blue,cyan,2)
        button("Settings",500,450,200,50,blue,cyan,3)


        pygame.display.update()
        clock.tick(15)


game_intro()

def paused():

    largeText = pygame.font.SysFont('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)


    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

pygame.quit()
quit()
