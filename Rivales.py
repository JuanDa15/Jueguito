import pygame
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
    
    def update(self):
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
              