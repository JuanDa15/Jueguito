import pygame
import random
width = 1080
high = 720

class Rival(pygame.sprite.Sprite):
    def __init__(self, position, velocityX, velocityY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Pelota Rival.png')
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y =position[1]
        self.velx = velocityX
        self.vely = velocityY
        self.timer = random.randrange(70,90)
    
    def update(self):
        self.timer -= 1
        self.rect.x+=self.velx        
        self.rect.y+=self.vely
        if(self.rect.x > width):
            self.rect.x = 0
        elif(self.rect.x < 0):
            self.rect.x = 1080
        if(self.rect.y > high):
            self.rect.x = 0
        elif(self.rect.y < 0):
            self.rect.y = 720

    def ReturnPosition(self):
        Xpos = self.rect.x - 23
        Ypos = self.rect.y + 15
        return [Xpos,Ypos]