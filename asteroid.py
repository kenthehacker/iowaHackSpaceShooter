import pygame
class Asteroid:
    pass
    def __init__(self, screen):
        self.height = 50
        self.width = 50
        self.speedy = 30
        self.speedx = 20
        self.screen = screen
        self.x=0
        self.y = 9

    def collisionDetection(self,otherObject):
        pass
    def getX(self):
        return self.x
        
    def getY(self):
        return self.y

    def moveAndDraw(self):
        BLUE=(0,0,255)
        pygame.draw.rect(self.screen, BLUE, (0,0, self.width, self.height))
        