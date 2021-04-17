import pygame
import sys
import os
import asteroid

pygame.init()

#pixel size of game
xSizeScreen = 700
ySizeScreen = 700

# set the fps
fps = pygame.time.Clock()

#variable dumps:
screen = pygame.display.set_mode((xSizeScreen, ySizeScreen))
running = True #runs the game until this is false
bg = pygame.image.load("spaceBackDrop.png")
pressSpaceText = pygame.image.load("text.png")
#example pressSpaceStuff = pygame.transform.scale(pressSpaceText,(width,height))

def splashScreen():
    screen.blit(bg,(0,-200))
    screen.blit(pressSpaceText, (-135,0))



while(running):
    fps.tick(60)
    splashScreen()
    s = asteroid.Asteroid(screen)
    s.moveAndDraw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()





